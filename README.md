<p align='center'><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Coat_of_arms_of_Hungary.svg/1200px-Coat_of_arms_of_Hungary.svg.png" alt="Magyarország címere" style="height: 210px; width:110px;"/></p>

# Magyarország települései

*Ez a repo tartalmazza Magyarország összes települését, vármegyék szerint, illetve a forrásfájlt, amivel ezeket az adatokat le tudjátok kérni.*

*A városnevek[^1], illetve irányítószámok pontosak (kell legyenek), a koordináták ritkán, de eltérhetnek a valóságtól.*

## Fájlok

``varmegyek-raw.json``: összes adat lekérve  

```json
"Bősárkány": {
    "varmegye": "Győr-Moson-Sopron",
    "iranyitoszam": 9167,
    "rang": "nagyközség",
    "szelesseg": 47.6881947,
    "hosszusag": 17.2507143
},
``` 

---

``varmegyek.json``: vármegyék szerint

```json
"Pest": {
    "Abony": {
        "iranyitoszam": 2740,
        "rang": "város",
        "szelesseg": 47.18854,
        "hosszusag": 20.0095688
    },
    "Acsa": {
        "iranyitoszam": 2683,
        "rang": "község",
        "szelesseg": 47.7946936,
        "hosszusag": 19.3864356
    },
},
``` 

---

Emellett az adatok elérhetőek **Excel** táblázatban is a könnyű böngészés érdekében.

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

### ⚠️ Figyelmeztetés ⚠️
A Google Maps API egy bizonyos kvótával rendelkezik, ami átlépése után díjat számolnak fel.

> *Google Maps Platform offers a $200 monthly credit for Maps, Routes, and Places (see Billing Account Credits). With the $200 monthly credit, some customers find their use cases are at no charge. You won't be charged until your usage exceeds $200 in a month.*


### Program futtatása

``iranyito.txt`` és ``varmegyek.py`` 1 mappába kell legyenek.  

```bash
py varmegyek.py -api API_KEY
```

Ez kettő fájlt fog legyártani, ezek példáit lásd [itt](#jelenlegi-adatok):
- ``varmegyek-raw.json``: az összes település neve, **minden lekért információval**.
- ``varmegyek.json``: az előbb lekért települések **vármegyék szerint** csoportosítva, ábécé sorrendben.

Az Excel fájlt a program beépített JSON import funkciójával csináltam.

### Tudnivalók
- A lefutási ideje jelenleg kb. 1 óra

- Google Maps API hibái:
    - 26 települést nem talál meg, így ezek koordinátáit sem tudja lehívni
    - Eperjes, Imola, Medina illetve Pula nevű települések koordinátái Magyarországon kívülre kerülnek, mert ezekre az első találat nem magyar település
- azaz **30 olyan település van, aminek az adatai hiányozni fognak, vagy hibásak lesznek** (ezeknek a száma olyan kicsi, inkább kézzel javítottam, mintsem megoldást találjak rá)

- a ``test`` mappába mellékeltem egy másik scriptet, ami lecsekkolja hány (biztosan) hibás település van, így ezeket kicsit könnyebben tudjátok javítani

## TODO
- [x] hibás településinformációk javítása
- [x] több adat lekérése
- [ ] több adattároló típus alkalmazása -> Excel, SQL DB, stb.

### Felhasznált források
[TÚRABÁZIS.hu](https://www.turabazis.hu/telepules_lista_0_0_n_n_n_n_0_n_0_n_0_n_n_n_n_0): települések és hozzájuk tartozó vármegyék nevei  
[Google Maps Places API](https://developers.google.com/maps/documentation/places/web-service): földrajzi szélesség és hosszúság  
Magyar Posta [Magyarországi postai irányítószámok](https://www.posta.hu/static/internet/download/Iranyitoszam-Internet_uj.xlsx) dokumentuma  
[Wikipédia](https://hu.wikipedia.org/wiki/Magyarorsz%C3%A1g_c%C3%ADmere): Magyarország címere kép

[^1]: Az összes nyilvántartásban szereplő település neve, összesen 3155 db település.
