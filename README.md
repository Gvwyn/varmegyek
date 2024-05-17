# Magyarország települései  

*Ez a repo tartalmazza Magyarország összes települését, vármegyék szerint, illetve a forrásfájlt, amivel ezeket az adatokat le tudjátok kérni.*

*A városnevek[^1], illetve irányítószámok pontosak (kell legyenek), a koordináták ritkán, de eltérhetnek a valóságtól.*

## Jelenlegi adatok

``varmegyek-raw.json``: összes adat lekérve  

```json
"Bősárkány": {
    "varmegye": "Győr-Moson-Sopron",
    "iranyitoszam": 9167,
    "hosszusag": 47.6881947,
    "szelesseg": 17.2507143
},
``` 

---

``varmegyek.json``: vármegyék szerint

```json
"Pest": {
    "Abony": { 
        "hosszusag": 20.0095688,
        "szelesseg": 47.18854
    },
    "Acsa": {
        "hosszusag": 19.3864356,
        "szelesseg": 47.7946936
    },
},
``` 

---

Emellett az adatok elérhetőek Excel formátumban is.

## Futtatás

*Ha szeretnél egy frissebb adatbázist, vagy csak ki akarod próbálni a forráskódot. Minden más esetben [itt](https://github.com/Gvwyn/varmegyek/releases) találod a legújabb verziót.* 

### Előfeltételek

- Python verzió 3.5+, csekkolás: ``py --version``
- alap Python könyvtárak: ``time, argsparse, json``
- illetve a következő nem alap Python könyvtárak:

```bash
pip install requests googlemaps BeautifulSoup4
```

- érvényes [Google Maps API](https://mapsplatform.google.com/) kulcs  

### Figyelmeztetés
A Google Maps API egy bizonyos kvótával rendelkezik, ami átlépése után díjat számolnak fel.

> *Google Maps Platform offers a $200 monthly credit for Maps, Routes, and Places (see Billing Account Credits). With the $200 monthly credit, some customers find their use cases are at no charge. You won't be charged until your usage exceeds $200 in a month.*

Az [Usage and billing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing) szekció alapján a program 1 teljes lefutása kb. $20-25. Ennek tudatában futtassátok a programot.


### Program futtatása

``iranyito.txt`` és ``varmegyek.py`` 1 mappába kell legyen.  

```bash
py varmegyek.py -api API_KEY
```

Ez kettő fájlt fog legyártani, ezek példáit lásd [itt](#jelenlegi-adatok):
- ``varmegyek-raw.json``: az összes település neve, **minden lekért információval**.
- ``varmegyek.json``: az előbb lekért települések **vármegyék szerint** csoportosítva.

Az Excel fájlt külön programmal csináltam, amit ez a kód nem tartalmaz.

## TODO
- [ ] async API call-ok, jelenleg több mint 1 óra a lefutási ideje a programnak
- [ ] több adat lekérése
- [ ] több adattároló típus alkalmazása -> Excel, SQL DB, stb.
- [ ] error handling

### Felhasznált források
[TÚRABÁZIS.hu](https://www.turabazis.hu/telepules_lista_0_0_n_n_n_n_0_n_0_n_0_n_n_n_n_0): települések és hozzájuk tartozó vármegyék nevei  
[Google Maps Places API](https://developers.google.com/maps/documentation/places/web-service): földrajzi szélesség és hosszúság  
Magyar Posta [Magyarországi postai irányítószámok](https://www.posta.hu/static/internet/download/Iranyitoszam-Internet_uj.xlsx) dokumentuma

[^1]: Az összes nyilvántartásban szereplő település neve, összesen 3179 db település.