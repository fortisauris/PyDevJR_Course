import hashlib
from session4 import FileTools

'''
 K O C K A  - HOD KOCKOU S OVLADANIM = rozcvicka
'''
import random

# naimportujeme random

# jednoduchu funkciu na Hod kockou

# nekonecneho cyklu
# a prikazu input() budeme programu zadavat prikazy
# ENTER, hodi kocku
# q quitne program

'''
G E N E R A T O R Y
'''

def semafor():
    """
    Jednoduchy generator nam generuje farby semafora.
    :return: farba - String
    """
    yield "cervena"
    yield "oranzova"
    yield "zelena"


svetla = semafor()  # Volame a spustame generator semafor
print(svetla)  # vytlaci nam generator objekt s adresou v pamati
print(next(svetla))  # vytlaci prvu hodnotu generatora
print(svetla.__next__())  # iny sposob ako vytlacit dalsiu hodnotu generatora
print(svetla.__next__())  # posledna hodnota generatora
# !!! POZOR !!! - na dalsej vyhodi chybu StopIteration... nas generator prisiel na koniec a treba ho znova spustit

svetla = semafor()  # Nova inicializacia
# for _ in svetla:  # prejdeme vsetky hodnoty generatora
#     print(svetla.__next__())



def generator_zoznamu():
    hodnoty = ["alpha", "bravo", "charlie", "delta"]  # zoznam moznych odpovedi
    yield random.choice(hodnoty)  # v tomto pripade funguje yield ako return a vrati nahodnu hodnotu

while True:    # nekonecny cyklus nam bude vraciat neustale hodnotu a resetovat sa
    alphacodes = generator_zoznamu()
    print(alphacodes.__next__())
    break


for _ in generator_zoznamu():
    print(_)

def fib(limit):  # jednoduchsie napisany fibonacciho rad pomocou generatoru
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


x = fib(50)  # spustime generator
print(list(x))  # moznost vlozit ich do listu
for _ in x:  # prejdeme vsetky hodnoty
    print(x.__next__())  # vytlaci dalsiu vypocitanu hodnotu

for i in fib(10):  # moznost vytiahnut hodnoty z generatora
    print(i)

# TODO Vyskusat vytvorit generator

"""
V I G E N E R O V A   S I F R A
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
posunuta_abeceda = lambda alphabet, shift: alphabet[shift:] + alphabet[:shift]
print(posunuta_abeceda(alphabet=alphabet, shift=3))

pripravene_heslo = lambda pwd, msg_len: (pwd*100)[:msg_len]
print(pripravene_heslo(pwd="hesloveslo", msg_len=15))

def vigenere_enc(sprava: str, pwd: str) -> str:
    """

    :param sprava:
    :param pwd:
    :return:
    """
    posuny = pripravene_heslo(pwd=pwd, msg_len=len(sprava))  # HOTELHOTELHOTELHO
    print("pripravene na sifrovanie :", posuny)  # reprezentacia pripraveneho hesla
    zasifrovany_text = ""  # nova premenna kde sa bude ukladat zasifrovany text
    for i in range(0, len(sprava)):  # prechadzame spravou pomocou for cyklu
        shift = alphabet.index(posuny[i])  # vypocitavame konkretny posun na znak
        enc_alphabet = posunuta_abeceda(alphabet, shift)  # pre kazde pismeno je nova posunuta abeceda
        symbol_value = enc_alphabet[alphabet.index(sprava[i])]  # vypocitavame hodnotu znaku v posunutej abecede
        zasifrovany_text += symbol_value  # pridavame znak do zasifrovaneho textu
    return zasifrovany_text  # vraciame zasifrovany text do hlavneho programu

text = "BRYNDZAZDRAZELA"  # text na zasifrovanie
vigenere = vigenere_enc(sprava=text, pwd="HOTEL")  # pouzivame nasu funkciu
print(vigenere)  # vytlacime do konzoly
print(vigenere_enc.__doc__)

# TODO Skuste spravit desifrovanie Vigeneroven sifry
# TODO Dorobit medzery v texte aby fungovali.

import itertools
import time

"""
M O D U L   I T E R T O O L S
"""

a = iter("ABCD")  # jednoduchy iterator pomocou zakladneho prikazu iter()
print(a)  # vytlaci iterator objekt a adresu v pamati
print(list(a))  # vytlaci vsetky hodnoty

zipsujeme = zip(["Jahody", "Maliny", "Cucoriedky"], [7.0, 9.0, 3.0])  # pomocou prikazu zip spoji dva listy
print(zipsujeme)
print(list(zipsujeme))

zipsujeme = zip(["Jahody", "Maliny", "Cucoriedky"], [54, 6546, 765, 757, 8768, 876, 868, 765, 6 ])
print(zipsujeme)  # spoji dva listy ale zbytok dlhsieho zoznamu zahodi
print(list(zipsujeme))

zipsujeme = itertools.zip_longest(["Jahody", "Maliny", "Cucoriedky"], [54, 6546, 765, 757, 8768, 876, 868, 765, 6 ],
                                  fillvalue=True)
print(zipsujeme)  # pomocou modulu itertools nahradime prazdne hodnoty hodnotou True
print(list(zipsujeme))

# Peniaze v penazenke
bankovky = [10, 50, 5, 100, 20]  # zoznam bankoviek v penazenke
print(list(itertools.combinations(bankovky, 3)))  # kombinacie

print(list(itertools.combinations_with_replacement(bankovky, 3)))  # kombinacie s opakovanim

a = "ABC"
print(list(itertools.permutations(a)))  # permutacie

counter = itertools.count()  # pocitadlo v itertoolse
while True:
    c = counter.__next__()  # positadlo ide do nekonecna...
    print(c)
    if c == 10:
        break
    time.sleep(.2)  # prikaz modulu time na pauzu v programe

c = itertools.count(start=.2, step=-.3)  # pocitadlo vie ist aj v desatinnych cislach aj negativne
print(list(next(c) for _ in range(5)))  # pythonisticky sposob ako vypisat 5 hodnot z pocitadla

opakovanie = itertools.repeat(1, 10)  # opakovanie cisel ... zobrazi 10 jednotiek
print(list(opakovanie))

opakuj_cyklus = itertools.cycle("ABCDE")  # pomocou itertools vieme opakovat sekvencie donekonecna
print(opakuj_cyklus)
for i in range(10):
    print(opakuj_cyklus.__next__())

a = [1,2,3,4,5]  # zoznam cisel
print(list(itertools.accumulate(a)))  # funkcia accumulate prirata hodnoty
print((list(itertools.accumulate(a, lambda x,y: (x+y)*2))))  # funkciu mozeme modifikovat pomocou lambda funkcie

a = itertools.product([1,2], ["A", "B"], [True, False])  # funkcia product
print(a)
print(list(a))

iterator1, iterator2, iterator3 = itertools.tee("ABCDEF", 3)  # funkcia tee vytvori naraz tri totozne iteratory
# ktore mozu rozne iterovat v programe
print(list(iterator1))
print(list(iterator2))
print(list(iterator3))

"""
JEDNODUCHY PROGRAM LIGA
"""

teams = ["Liverpool", "FC Barcelona", "Manchester", "AJAX Amsterfam"] # zoznam timov
zapasy = itertools.combinations(teams, 2)  # itertools nam vytvori kombinacie zapasov
liga = dict()  # vytvorime premennu Slovnik
for i in zapasy:  Postupne vytahujeme zapasy
    zapas = zapasy.__next__()  # pomocou next
    key = zapas[0]+":"+zapas[1]  # skladame klucove slovo slovnika
    print(key)  # kontrolujeme ho
    liga[key] = [0, 0]  # vkladame defaultny stav zapasu 0:0

print(liga)  # vytlacime si slovnik

# TODO prestavka do 20:00

"""
 PROGRAM NA ZAPAMATANIE   JE CISLO PARNE ?
"""

def je_cislo_parne(n: int) -> bool:

    if n/2 == int(n/2):  # logicky blok porovnava ci je cislo delene dvoma cele, alebo bol odstraneny zostatok
        return True  # ak nie je zostatok vrati PRAVDA
    else:
        return False  # ak je zostatok vrati NEPRAVDA

for i in range(0,50):
    print(i, je_cislo_parne(i))

"""
JEDNODUCHY LUSKAC HESIEL
"""


def hash_it(text: str):  # jednoducha funkcia na vypocet hashstringu zo zadaneho textu HASLA
    """
    Jednoducha funkcia fungujuca ako MIXER, vkladame do nej data v podobe bytov a algoritmus
    MD5 ich neustale prepocitava
    :param text:
    :return: hexadecimaly hashstring algoritmu MD5 jedinecny otlacok vstupnych dat
    """
    h = hashlib.md5()  # vytvorenie objektu hashovacieho algoritmu
    data = bytes(text, encoding="utf8")  # pripravime si data
    h.update(data)  # nasypeme ich do Algoritmu
    return h.hexdigest()  # vratime hexadecimalny vystup

# Na urcenie mnoziny moznych hesiel potrebujeme informacie o Jozefovi
Jozef = ["Kapor", 1986, "Octavia", "Slovan", "Maj", 12, "Chorvatsko", 2023, "Janka", "Dominik", "Jozef"]
# TODO Spravit a vyskusat viacere osoby


def PwdCracker(Person: list):
    """
    Jednoduchy program, ktory vypocita mnozinu moznych jednoduchych hesiel na zaklade zistenych informacii.
    :param Person: zoznam moznych pouzitych slov : list
    :return: # zoznam moznych hesiel
    """
    dvojice = itertools.combinations(Jozef, 2)  # pomocou modulu itertools spravime kombinacie dvoch slov
    raw_data = list(dvojice)  # nazvime ich surove data
    result = []  # vysledkom programu bude zoznam
    for cast1, cast2 in raw_data:  # vytahujeme obe slova z kombinacie
        result.append(str(cast1) + "1")  # pouzijeme prve slovo plus cislo 1
        result.append(str(cast2) + "1")  # pouzijeme druhe slovo plus 1
        result.append(str(cast1)+str(cast2))  # pouzijeme obe slova spojene
        result.append(str(cast2)+str(cast1)) # pouzijeme obe slova opacne
        result.append(str(cast2).upper() + str(cast1).upper())  # pouzijeme obe slova Velkymi pismenami
        result.append(str(cast2).lower() + str(cast1).lower())  # pouzijeme obe slova malymi pismenami
        result.append(str(cast2) + str(cast1)+"1")  # pouzijeme obe slova plus 1
        result.append(str(cast2) + str(cast1) + "2")  # pouzijeme obe slova plus 2
        result.append(str(cast2) + str(cast1) + "2022")  # pouzijeme obe slova plus aktualny rok
    print(result)  # vytlacime zoznam
    print("POCET ODHADOVANYCH HESIEL:", len(result))  # vytlacime pocet moznych kombinacii slov
    return result  # vratime zoznam do hlavneho programu

result = PwdCracker(Person=Jozef)  # zavolame funkciu a  dame jej data
prepared_text_output = ''  # pripravime si vystupny text pre subor
for i in result:  # prejdeme vysledky zoznamu hesiel
    prepared_text_output += i + "\n"  # postupne pridame heslo a specialny znak na novy riadok
FileTools.file_save(filename_w_path="hesla", plaintext=prepared_text_output)  # pomocou nainportovaneho nastroja ulozime hesla


# N8vzd7_Sa:Zach0V8:VPAM*tI_Stu!k0v8  LAHKO ZAPAMATATELNE A PRITOM TAZKO UHADNUTELNE HESLO
