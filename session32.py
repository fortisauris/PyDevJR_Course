'''
SESSION 32 - ADVANCED FASTAPI FILE UPLOAD AND SECURITY

Dokončenie FA05

Validacia, response_model,

File Upload pomocou metody POST a importovaných objektov z fastapi
Ukladamé binárne súbor aj s jeho názvom na cieľový server pomocou http protokolu.

Treba doinštalovať  - pip install python-multipart

FA06 Ochrana Route pomocou fastapi_simple_security

Treba doinštalovať - pip install fastapi-simple-security

Všetky routy tykajuce sa autentifikacie su predprogramovane.

Pridame router fastapi_simple_security a máme hotovo

Chránená route je závislá na schvlálení prístupu pomocou vzgenereovaného API kľúča.

Pri štarte fastapi_simple_security sa vygeneruje kľúč pre Admina

Pomocou neho vieme vytvoriť kľúč pre užívateľa, ktorý sa ukladná do databázy sqlite.db

Ak sa identifikujeme kľúčom užívateľa môžeme vstupovať k chránenej api.
Kľúč sa automaticky kopíruje v ďalších requestoch v hlavičke alebo v query GET requestu


Prezeráme databázu pomocou modululu sqlite3

V súbore pozri_db.py sme vytvorili jednoduchý skript na prezeranie uložených hesiel v sqlite.db

Prezeranie funguje na  základe pripojenia connection k databázovému súboru

a následne určeniu kurzoru cur, ktorý zadáva operácie databáze.

takto môžeme manipulovať s dátami v databáze bez toho aby sme spustili konzolu sqlite


FA06 Ochrana routes pomocou fastapi_login

treba doinštalovať = pip install fastapi-login

Fastapi login obsahuje predprogramované rozhranie na generovanie API kľúčov pre užívateľov.

Pomocou Login managera a funkcie na načítavanie Usera z databázy (v podobe dict())

vytvárame login formulár pre autentifikáciu užívateľa pomocou mena a hesla.

Tento formulár nám vygeneruje API klúč v podobe TOKENU.

Token je potom zasielaný v rámci requestu (pravdepodobne v JWT)

Ak chceme prístup k chránenej api route tak treba sa autentifikovať pomocou mena a hesla.

Bearer = Nositeľ potom pošle API kľúč v requeste v tokene a prístup je povolený.


requirements.txt

requirements.txt by mali obsahovať softvér, ktorý je potrebné do pythonu3 doinštalovať

napr:
fastapi
uvicorn
jinja2

priíkazom pip install -r requirements.txt

sa automaticky nainštalujú všetky tzv. Dependencies

príkazom pip freeze
zistíme čo máme nainštalované vo venv

POZOR pip freeze > requirements.txt NEPOUŹÍVAJTE
teda pokiaľ nechcete mať plné obálky zastaralých balíčkov plných zraniteľností a legacy kódu.
'''