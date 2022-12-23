'''
SESSION29 - FLASK UKLADANIE DAT, STRUKTURA PROJEKTU, BLUEPRINTS a LOGIN MANAGER

FL03 - dokoncenie

V FL03 sme si ukazali ako ukladat data lokalne do zoznamu alebo slovnika, no po restarte naseho Flskoveho servera nam
vsetko zmizne a zacina sa ukladat v pamati nanovo. Vyuzivame tiez vstavany slovnik session do ktoreho mozeme ukladat data.

!!! DATA v session sa ukladaju v uzivatelovom browseri vo forme Cookies a preto nemozu obsahovat data vacsie ako 4kb a
zaroven tam NESMIEME ukladat citlive informacie - mena, hesla a pod. Mozu obsahovat iba META data a nepodstatne polozky
z formularov

#FL04

v FL04 sa pokusame tieto veci riesit:
1. Ukladanim dat z session do suboru pomocou modulu json

    ## Flask ma vlastnu funkciu jsonify, ktora vie rychlo zmenit premennu na json.

    !!! POZOR ked je viac uzivatelov nebude pocitac stihat zapisovat zmeny

2. Naimportovali sme si Session s velkym S, ktoru sme doinstalovali z balicka flask_session. Tato velka SESSION sa uklada
 na nasom serveri. Pristupujeme k nej vylucne cez malu session. Je to vlastne zjednodusene povedane zrkadlo malej session.

 Okrem ineho obsahuje aj metody na prepojenie s dalsimi databazami. My sme ukladali data v hexadecimalnom formate do
 suborov

 !!! POZOR je to lepsie ako json ale opat moze nastat problem, ze ked bude uzivatelov privela aplikacia nebude stihat
 zapisovat

3. Pouzijeme jednosuborovu SQL databazu sqlite3 a modul pythona sqlite3 na manipulaciu s nou. Toto riesenie je dostacujuce
pre male appky kde nie je vela Trafficu a nevznikaju dopravne zapchy:)

!!! Databazu sqlite treba stiahnut a nainstalovat do PC. Treba nastavit tiez systemovy PATH. Windowsu sa to moc nepaci.

4. POuzijeme velku SQL databazu ako MySQL(MariaDB) alebo PosgreSQL. Databaza umoznuje vytvarat databazy priamoz modelov
vo Flasku, zapisovat a manipulovat pomocou lib SQLAlchemy.

!!! IDE O PREFEROVANE RIESENIE PRE UKLADANIE STRUKTUROVANYCH DAT ZORADENYCH V TABULKACH - JEdnoduchy tutorial pripojeny

5. Pouzijeme NonSQL databazu - ukazali sme si na nasom serveri Redis, ktory uklada data podobne ako sa ukladaju pythonovske
premenne - Jednoduchy tutorial bude pripojeny.

!!! POZOR na rozdiel od MySQL Redis neumoznuje viacero uzivatelov a pristup chrani jednoduchym HESLOM.

# Umiestnenie databazy by malo byt kvoli rychlosti co najblizsie k Flaskovej appke kvoli rychlosti zapisu a citania.

6. Pripravili sme pre Vas malicky server kde je sqlite3, MySQL aj redis na IP adrese :

pripojite sa nan pomocou prikazu:
                                        ssh pydev2022@188.121.170.77

Heslo pre ucastnikov kurzu na vyziadanie mailom. Server bude pristupny 6 mesiacov a je urceny vylucne na studijne ucely.


# FL05

V FL05 si ukazujeme moznosti strukturovania naseho projektu. Prenasame app kontext do dalsieho adresara app. Kde mozeme
vytvarat viacero suborov z cestami, db modelmi atd. Vsetko co je vo Flaskovom app kontexte je mozne zavolat a
naimportovat.

BLUEPRINTS du Flaskove samostatne podaplikacie. Su vytvorene v samoztatnom adresari a s app kontextom su spojene pomocou
registracie. Maju vlastne templates aj static. Mozu byt rychlo implementovane do noveho flaskoveho projektu. Routes v
Blueprintoch vyuzivaju tzv. url_prefix a su tak oddelene od vsetkych @app.route().


# FL06

Vo FL06 si ukazujeme ako pomocou doinstalovaneho flask_login vyuzivame LoginManagera na prihlasovanie do Flaskovej appky.
Vsetky routes oznacene dekoratorom @login_required su pristupne iba nalogovanym uzivatelom.

Pomocou current_user.id vieme zistit o akeho uzivatela ide.
DOMACA ULOHA: Skuste spravit route pristupny len pre urciteho uzivatela

!!! INFORMACIA OHLADNE PROJEKTU Cosmic1

git clone https://github.com/fortisauris/Cosmic1.git

si stiahnite repozitar z Githubu.
Zaslite mi mailom vas github username na pripojenie aby ste mohli na nom pracovat. Vsetky info a instrukcie na Workflow
najdete v README.md

PRAJEM VSETKYM STASTNE A VESELE VIANOCE A VSETKO DOBRE DO NOVEHO ROKU - ROKU PYTHONA :)

'''