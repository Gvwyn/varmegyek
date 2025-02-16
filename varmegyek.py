import argparse, json, time, requests, googlemaps
from bs4 import BeautifulSoup

# uzenet mindenkinek
# a kod angolul van, mert nem tudok magyarul elnevezni dolgokat

api_key = ''

pages = 158                         # number of pages as of 5/16/2024
towns = 3155                        # total number of towns
towns_checked = 0                   # incremented value for feedback

outputfile = 'varmegyek-raw.json'   # output file
sortedfile = 'varmegyek.json'       # sorted output file by counties
output = {}                         # output

# parse the town names & their counties from the page
def getTownsFromPage(url):
    global towns, towns_checked
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        td_elements = soup.select('td.oszlopbal9vastag')
        for td in td_elements:
            town_name = td.text.strip()
            towns_checked += 1;

            if "kerület" in town_name or "külföld" in town_name: 
                print(f'{towns_checked}/{towns} {towns_checked / towns * 100: .4f}%\t({town_name})')
                continue

            county_name = td.find_next_sibling('td', class_='oszlopkozep7').find_next_sibling('td', class_='oszlopkozep7').text.strip()
            type_name = td.find_next_sibling('td', class_='oszlopkozep7').find_next_sibling('td', class_='oszlopkozep7').find_next_sibling('td', class_='oszlopkozep7').text.strip()
            postal_code, latitude, longitude = getTownDetails(td.text.strip())
            
            output[town_name]= {
                'varmegye': county_name,
                'iranyitoszam': int(postal_code),
                'rang': type_name,
                'szelesseg': latitude,
                'hosszusag': longitude
            }
            print(f'{towns_checked}/{towns} {towns_checked / towns * 100: .4f}%\t{town_name}')
    else: print(f'Uh oh...\n{url} -> {response.status_code}')

# this is the google maps api magic
# gather data about each town and return it
def getTownDetails(location):
    # default values
    latitude = 0;
    longitude = 0;
    postal_code = '0'
    if (location in towns_set): postal_code = towns_dict[location];
    #return postal_code, 0, 0 # uncomment this to run without api call
    mapClient = googlemaps.Client(key=api_key)
    results = mapClient.places(location)
    if results['status'] == "OK":
        latitude = results['results'][0]['geometry']['location']['lat']
        longitude = results['results'][0]['geometry']['location']['lng']
        
    return postal_code, latitude, longitude


# eenie meenie miny moe
parse = argparse.ArgumentParser();
parse.add_argument('-api', dest='api_key', metavar='API_KEY', type=str, required=False, help='Google Maps API Key')
args = parse.parse_args()

# only use the passed arg API key if it wasnt defined before
if api_key == '':
    api_key = args.api_key
    try:
        googlemaps.Client(key=api_key)
    except googlemaps.exceptions.ApiError:
        raise SystemError('Helytelen API kulcs.')

start = time.time()

# read postal codes file -> iranyito.txt
towns_dict = {}
print('"iranyito.txt" beolvasasa... ', end='')
with open('iranyito.txt', 'r', encoding='utf-8') as file:
    for line in file:
        postal_code, *fucked_up_town = line.split()
        fixed_town = ' '.join(fucked_up_town)
        towns_dict[fixed_town] = postal_code

# this saves some time i think
towns_set = set(towns_dict.keys())
print('KESZ!')

for index in range(pages+1):
    url = f'https://www.turabazis.hu/telepules_lista_0_0_n_n_n_n_0_n_0_n_0_n_n_n_n_{index}'
    getTownsFromPage(url)

end = time.time()

sorted_output = {}
for town, details in output.items():
    county = details['varmegye']

    if county not in sorted_output:
        sorted_output[county] = {}
    
    sorted_output[county][town] = {
        'iranyitoszam': details['iranyitoszam'],
        'rang': details['rang'],
        'hosszusag': details['hosszusag'],
        'szelesseg': details['szelesseg']
    }

sorted_output = dict(sorted(sorted_output.items()))

# print(output)
with open(outputfile, 'w', encoding='utf-8') as json_file:
    json.dump(output, json_file, indent=4, ensure_ascii=False)

with open(sortedfile, 'w', encoding='utf-8') as json_file:
    json.dump(sorted_output, json_file, indent=4, ensure_ascii=False)

print(f'\n\nLefutott. {(end - start): .2f} másodperc\nFájlok: {outputfile}, {sortedfile}')
