import http.client
import json

'''
Jednoduchy http client na stahovanie html kodu pomocou metody GET z internetu.
'''
con = http.client.HTTPSConnection("fortisauris.com")  # HTTP a HTTPS
con.request("GET", "/")
r1 = con.getresponse()  # urob volaco
headers = r1.getheaders()
print(r1.status, r1.reason)
print("HEADERS :\n", headers)

obsah = r1.read(500)
print(obsah)

'''
Jednoduchy http klient, ktory pomocou PUT vklada na server udaje
'''

BODY = '*** CONTENT ***'
con = http.client.HTTPConnection('localhost', 8000)
con.request('PUT', '/file', BODY)
response = con.getresponse()
print(response.status, response.reason)

# TODO Metoda DELETE - Nastudovat
# TODO Metoda PATCH - Nastudovat

'''
Jednoduchy http klient, ktory pripravuje request POST a posiela udaje na server alebo do formulara
'''

# {  # typicke vyuzitie metody POST
#    'login':'uzivatel45',
#    'password':'bryndz123'
#    }


con = http.client.HTTPSConnection('www.httpbin.org')  # server na testovanie http requestov
headers = {'Content-type': 'application/json'}

foo = {'text': "TOTO JE NAS TEXT"}
json_data = json.dumps(foo)

con.request('POST', '/post', json_data, headers)
res = con.getresponse()
# print(res.read().decode())

'''
Jednoduchy http klient pomocou kniznice urllib
'''

import urllib.request

with urllib.request.urlopen("https://fortisauris.com") as f:
    obsah = f.read().decode('utf8')
    print(obsah)
'''
# R O Z C V I C K A  - H L A D A N I E  V   H T M L  K O D E
# pomocou htttp.clienta alebo urllib otvorit stranku
# pomocou metody GET ziskat html
# vybrat z html kodu vsetky linky

# najdete emailove adresy alebo linky
# 'href='
# 'src='
# '@'
# LINKY
# EMAILY
'''
'''
jednoduchy klient, ktory nacitava obsah stranky pomocou GET
'''
con = http.client.HTTPSConnection("fortisauris.com")  # HTTP a HTTPS
con.request("GET", "/")
r1 = con.getresponse()  # urob volaco
headers = r1.getheaders()
print(r1.status, r1.reason)
print("HEADERS :\n", headers)

obsah = bytes(r1.read()).decode('utf8')
print(obsah)


'''
D E K O R A T O R Y  A  F U N K C I E   V Y S S I E H O  R A D U

@staticmethod  - Basic Class - staticka metoda bez pouzitia premennych triedy pristupna aj bez iniciacie
@classmethod  - Basic Class - Metoda triedy, ktora nepouziva premenne triedy a moze byt vyuzita bez jeje iniciacie
@property - Advanced Class - Metoda triedy, ktora oznaci metodu ako majetok a zacne sa spravat ako premenna triedy
'''



def hello(func):

    def wrapper():  # toto je vnutorna funkcia
        print("UROB NIECO PRED VLOZENOU FUNKCIOU")
        func()
        print("UROB NIECO PO SKONCENI VLOZENEJ FUNKCIE")

    return wrapper

@hello
def nasa_funkcia():
    print("UROB VOLACO")


# hello(nasa_funkcia)
nasa_funkcia()  # volame nasu funkciu

'''
F U N K C I A   D E K O R A T O R A  S  P A R A M E T R A M I (*args, **kwargs)
'''


def hello(func):

    def wrapper(*args, **kwargs):   # vsetky argumenty a kvaziargumenty
        print("UROB NIECO PRED VLOZENOU FUNKCIOU")
        func(*args, **kwargs)
        print("UROB NIECO PO SKONCENI VLOZENEJ FUNKCIE")

    return wrapper


@hello
def pozdrav(meno: str, pocet: int):
    for i in range(pocet):
        print("AHOJ", meno)

pozdrav("Jozko", 3)  # volame nasu funkciu

'''
Dekorator @salba sa nas snazi presvedcit, ze 2 a 2 nie su 4 !
'''

def salba(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 1

    return wrapper

@salba
def spocitaj(a,b):
    return a + b


print(spocitaj(2, 2))

'''
Priklad vyuzitia dvoch dekoratorov sucasne
'''


def decor1(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper

def decor2(func):
    def wrapper():
        x = func()
        return x * 2
    return wrapper

@decor1
@decor2
def num():
    return 10

print(num())  # volame nasu dvojdekorovanu funkciu

'''
PRIKLAD VYUZITIA DEKORATORA PRI VYKONANI ULOZENIA NASTAVENI VYZADUJE ABY UZIVATEL BOL ADMIN
'''

USER = "admin"

def admin(func):

    def wrapper(*args, **kwargs):
        if USER == "admin":
            func(*args, **kwargs)
            print("NASTAVENIA ULOZENE")
            return True  # flag
        else:
            print("UZIVATEL ",USER ," NEMA OPRAVNENIE UKLADAT ZMENY")
            return False

    return wrapper

@admin
def uloz_nastavenia_serveru():
    print("CONFIG ULOZENY")

uloz_nastavenia_serveru()  # volame ulozenie nastaveni servera

# a = admin(uloz_nastavenia_serveru)
# print(a())
'''
P A L I N D R O M  A L G O R I T M U S- Slovo, ktore je rovnake odzadu aj odpredu
'''

s = 'bryndza'


def palindrome(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]:
            return True
    return False

# print(palindrome(s))


# E N I G M A   P L U G B O A R D

def plugboard(mods: dict, key):

    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    defaultne_nastavenie = dict(zip(abeceda, abeceda))
    # print(defaultne_nastavenie)
    defaultne_nastavenie.update(mods)
    # defaultne nastavenie sa zmeni na modifikovane nastavenie
    # print(defaultne_nastavenie)
    return defaultne_nastavenie[key]

# NASTAVENIE MODIFIKACII NA PLUGBOARDE
mods = {"A":"Z",
        "Z": "A",
        "Y": "C",
        "C": "K",
        "K": "Y"
        }
'''
msg = "BRYNDZAZDRAZELA"
enc_msg = ""
for i in msg:
    enc_znak = plugboard(mods=mods, key=i)
    enc_msg += enc_znak
print(msg, "\t", enc_msg)
'''
# TODO Prestavka do 20:05

'''
E N I G M A  - pridame si dalsi rotor
'''

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sprava = "BRYNDZAZDRAZELABRYNDZAZDRAZELA"

i = abeceda.index("R")  # pociatocne nastavenie valca
nastaveny_valec_1 = abeceda[i:] + abeceda[:i]
print(nastaveny_valec_1)

i = abeceda.index("S")  # pociatocne nastavenie valca
nastaveny_valec_2 = abeceda[i:] + abeceda[:i]
print(nastaveny_valec_2)

i = abeceda.index("F")  # pociatocne nastavenie valca
nastaveny_valec_3 = abeceda[i:] + abeceda[:i]
print(nastaveny_valec_3)


def posun_valca(nastaveny_valec):
    valec = nastaveny_valec[1:] + nastaveny_valec[0]
    print(valec)
    return valec


zasifrovana_sprava = ""
posun_valcov = 0
for i in range(0, len(sprava)):
    enc_znak = nastaveny_valec_1[abeceda.index(sprava[i])]  #
    enc_znak = nastaveny_valec_2[abeceda.index(enc_znak)]
    enc_znak = nastaveny_valec_3[abeceda.index(enc_znak)]
    # TODO Reverzny valec
    enc_znak = plugboard(mods=mods, key=enc_znak)  # Plugboard
    nastaveny_valec_1 = posun_valca(nastaveny_valec_1)

    if posun_valcov == 26:
        nastaveny_valec_2 = posun_valca(nastaveny_valec_2)  # TODO Ak Valec 2 dosiahne 26 ???
        posun_valcov = 0
    zasifrovana_sprava += enc_znak
    posun_valcov += 1

print(sprava)
print(zasifrovana_sprava)
# vysledok bez plugboardu: PGOEVSUUZOYYEMCEVDTKHJJODNNUCS
# vysledok s plugboardom:  PGOEVSUUAOCCEMKEVDTYHJJODNNUKS


