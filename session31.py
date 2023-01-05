'''
SESSION31 - FASTAPI ADVANCED

Dokončujeme FA02 načítavanie cien BTC z inej API.

Postupne vytvárame tri routy pre kurz USD, GBP a EUR

Projekt FA03_METEO

Pokračujeme v FA03 kde robíme projekt ktorý bude načítavať počasie z inej API.

Tento náš program využíva tzv Async funkcie, ktoré umožňujú pythonu pokračovať v programe aj keď
samotná funkcia Async čaká na odpoveď z Internetu. To znamená, že počítač nejde naprázdno a
pracuje naplno aj keď čaká na pomálý internet.

Najprv si vytvárame jednoduchú route v main_hello.py

Potom sa púšťame do komplikovanejšieho projektu a pomocou Jinja2Templates renderujeme
cieľ routy do html kódu.

Treba nanštalovať do venv(virtualnej obalky) jinja2 pomocou pip install jinja2

Treba nastaviť aby FastAPI vedel nájsť miesto kde sú umiestnené templates

Treba vytvoriť html template

FastAPI pozná niečo ako Blueprints vo Flasku... sú to samostatné programy, ktoré sa prepoja z našim
app kontextom = rozumej Flasou. V FastAPI ich nazývame APIRoutery = smerovače

Smerovač má vlastný kontext a jednotlive Routes nezačínajú app.get ale router.get

V maine ich pripojíme k app kontextu importovaním a registráciou routera

Vytvárame cestu, ktorá nám bude z inej API naťahovať počasie. Táto API potrebuje Geolokačné dáta
lat, lon aby vedela načítať dáta.

Vytvárame preto jednoduchú databázu miest kde do Slovníka pridávame mestá a koordináty.

Ak mesto nie je v databáze funkcia nám vráti odpoveď, že také mesto nepozná.

Program funguje a my potrebujeme zo získaných dát vytiahnuť iba tie, ktoré nás zaújimajú.

To je konkrétne teplota.

Funkcia našeho programu nám dáva teplotu v danom meste. Aby sme k tomu dali nejakú pridanú hodnotu
vytvárame jednoduchú logiku, ktorá nám okrem teploty zobrazí aj info či si máme obliecť MIKINU.

Na záver donútime funkciu validovať výsledok pomoocu modelu v models. Akonáhle funkcia nemá všetko
potrebné začne vyhazdovať chybu... teplota a mikina.


Projekt FA_04 Validator, Query

Vytvorime si jednoduchu Route s funkciou ktora ukazuje STATUS globalnu premennu, ktora sa meni.

Vytvorime si jednoduchy pydantic BaseModel pre naše statusové hlásenie. Vieme v rámci samotnej klassy
ošetriť validáciu pomocou Field ako sme to robili doteraz. Ale tentokrat si pridávame vlastný
validátor v podobe. Potrebujeme naimportovať dekorátor validator.

Validácia kontroluje či sa číselný kód statusu nachádza v zozname. Ak je všetko je v poriadku
Ak nie je vyhodí ValueError

Ďalšia vec, ktorú si ukazujeme je práca z QUery.
Naša funkcia naďalej posiela informácie o statuse no deginovaním q  určujeme, že môže prijimať
argumenty cez GET request.

Vkladáme do nej rozme argumenty rozdelené čiarkou...
Vo funkcí ich pomocou cyklu for vyťahujeme a dokážeme ich použiť v rámci programu.



'''