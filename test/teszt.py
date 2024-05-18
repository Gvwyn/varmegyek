import json


with open('varmegyek-raw.json', 'r', encoding='utf-8') as fajl:
    poo = json.load(fajl)

total = 0
north = []
south = []
east = []
west = []

empty_total = 0
empty_coords = []

for key in poo.keys():
    # ha nincs koordinataja
    if poo[key]['szelesseg'] == 0:
        empty_coords.append(key)
        empty_total += 1
        continue

    # legeszakibb telepulesen tul van
    if 48.585217 < poo[key]['szelesseg']: 
        north.append(key)
        total += 1
        continue

    # legdelibb telepulesen tul van
    if 45.775223 > poo[key]['szelesseg']:
        south.append(key)
        total += 1
        continue

    # legkeletibb telepulesen tul van
    if 22.8770579 < poo[key]['hosszusag']:
        east.append(key)
        total += 1
        continue

    # legnyugatibb telepulesen tul van
    if 16.1381951 > poo[key]['hosszusag']:
        west.append(key)
        total += 1

print(f'ossz: {total}\nE: {north}\nD: {south}\nNY: {west}\nK: {east}\n\nures koordinata: {empty_total} db\n{empty_coords}')