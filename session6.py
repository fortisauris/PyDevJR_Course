'''
SESSION6 - ZAKLADY FUNKCIONALNEHO PROGRAMOVANIA, MODUL OPERATOR, XOR ENCRYPTION, ZETTELKASTEN

Funkcionalne programovanie nam namiesto proceduralnych krokov umoznuje pomocou funkcii dopracovat sa
rychlejsie k vysledku.

prikaz zip()
prikaz map()
prikaz filter()
prikaz sort() a sorted()

Funkcionalne programovanie casto vyuziva lambda funkcie.
Modul operator nam poskytuje obravske mnozstvo predrobenych operacii vhodnych do lambda funkcii

XOR Encryption - Sifrovanie pomocou logickej operacie XOR medzi dvoma bytami.
                Vyhody - rychlost, dlzka spravy sa nemeni, vyuzitie hesla aj jedinecneho OTP kluca
                Nevyhody - entropia kluca musi byt velka, distribucia nezapamatatelneho kluca,


ZettelKasten,  - system karticiek na zapamatanie si poznatkov. Predstavujeme si format MarkDown.
                Karticky su prepojene pomocou linkov

'''

import functools
import operator
from session4 import abeceda
'''
KAMEN PAPIER NOZNICE  S UKLADANIM VYSLEDKOV
'''

# naimportuj zo session4 FileTools
# from session4 import FileTools

# nekonecny cyklus while True

# premennu zoznam kde bude KAMEN PAPIER NOZNICE

# premennu na ukladanie vysledkov String

# pouzit prikaz input()

# naimportujeme si random

# pouzijeme random.choice()

# print do konzoly vysledok

# logicky blok if "q" ulozi subor "KPN.txt"

# break ukonci program

'''
ZAKLADY FUNKCIONALNEHO PROGRAMOVANIA
'''

# Rozdiely

a = ["A", "B", "C", "D", "E"]

# tradicny pristup
result = []  # prazdny zoznam
for i in a:
    result.append(i.lower())
print(result)

# funkcionalne programovanie v pythone
pismena = list(map(lambda x: x.lower(), a))
print(pismena)

cisla = [3.5, 12.65, 34.78, 11.87]
result = list(map(round, cisla))
print(result)

funkcia = lambda x: round(x /2 )
result = list(map(funkcia, cisla))
print(result)

cisla2 = [7.54, 7.243, 12.87, 1.87]
result = list(map(lambda x,y: x/y, cisla,cisla2))
print(result)

viac_ako_tri = list(filter(lambda x: x >3, cisla2))
print(viac_ako_tri)

mena = ["Gregor", "Yveta", "Jozef", "Frantisek"]
obsahuje_pismeno = list(filter(lambda x: "r" in x, mena))
print(obsahuje_pismeno)

# ULOHA SPravte tri mapy a tri vlastne filtre

redukovany_zoznam = list(functools.reduce(lambda x,y: x + y, mena))
print(redukovany_zoznam)


def spojeny_string(string1, string2):
    return string1 + string2

text = ["A","H","O","J"]
final_string = functools.reduce(spojeny_string, text)
print(final_string)
print(type(final_string))

nlist = [[1,2,3], [4,5,6], [7,8,9]]
flist = functools.reduce(lambda a,b : a+b, nlist)
print(flist)

"""
MODUL O P E R A T O R
"""
a = list(map(operator.add, [1,2,3], [432,87,543]))
print(a)

a = list(map(operator.sub, [1,2,3], [432,87,543]))
print(a)

a, b = 12, 34
res = operator.mul(a,b)
print(res)

a, b = 12, 34
res = operator.truediv(a,b)
print(res)

a, b = 12, 34
res = operator.floordiv(a,b)
print(res)

a, b = 12, 34
res = operator.mod(a,b)
print(res)

a, b = 12, 34
res = operator.pow(a,b)
print(res)


"""
POROVNAVACIE FUNKCIE
"""
a, b = 12, 34
res = operator.lt(a,b)  # Less Than Menej ako
print(res)

a, b = 12, 34
res = operator.gt(a,b)  # Greater Than Viacej ako
print(res)

a, b = 12, 34
res = operator.ge(a,b)  #Greater OR Equal  Vacsie alebo rovne
print(res)

a, b = 12, 34
res = operator.le(a,b)  # Less or equal  Menej alebo rovne
print(res)

a, b = 12, 34
res = operator.eq(a,b)  # Equal Rovne
print(res)

a, b = 12, 34
res = operator.ne(a,b)  # None Equal Nerovne
print(res)

"""
BITWISE OPERACIE  0000000-11111111, 00-FF, 0-255
"""
a = 255
res = operator.invert(a)
print(res)

res = operator.contains(mena, "Yveta")
print(res)

cisla = [134, 65, 543, 765, 32]
zoradene_cisla = sorted(cisla, reverse=True)
print(zoradene_cisla)

text = "Bryndza zdrazela"
print(sorted(text.lower()))
print(sorted(text.split(" ")))

# map
# filter
# sorted
# reduce

'''
PASCALOV TROJUHOLNIK
'''
n = 5
for i in range(n):
    print(" " * (n-1), end='')
    print(" ".join(map(str, str(11**i))))

import itertools

demo_hodnoty = itertools.combinations_with_replacement([True, False], 2)
print(list(demo_hodnoty))

for i in demo_hodnoty:
    print(i)

demo_hodnoty = itertools.combinations_with_replacement(['0b00000000', '0b11111111'], 2)
print(list(demo_hodnoty))

for i in demo_hodnoty:
    print(i)

# ^ XOR  -
# kluc XOR spravu = zasifrovana sprava
# zasifrovana sprava XOR kluc = sprava


def xor_enc(sprava: str, heslo: str) -> str:
    """

    :param spravu:
    :param heslo:
    :return:
    """
    enc_sprava = ""  # prazdva premenna kde sa budu pridavat zakryptovane pismena
    prepared_heslo = (100*heslo)[:len(sprava)]  # pripravene heslo !!! POZOR !!! rovnako dlhe ako sprava
    print(sprava, prepared_heslo)  # kontrolny print do konzoly
    for i in range(0, len(sprava)):  # prechadzame spravou
        enc_value = abeceda.index(sprava[i]) ^ abeceda.index(prepared_heslo[i])  # Pomocou funkcie Bitwise XOR
        # scitavame indexy pismen
        enc_sprava += str(enc_value) + " "  # prida vysledok a medzeru
    return enc_sprava  # vrati zasifrovany text v podobe cisel.

#  Prestavka do 20:00

print(xor_enc("BRYNDZAZDRAZELA", "HOTEL"))

# ULOHA Spravit desifrovanie
# ULOHA Skusit sa zamysliet ako Cracknut tuto sifru.

'''
ZETELLKASTEN system
'''
import random

baza_dat = dict()

def generuj_id():
    """

    :return:
    """
    id = random.randint(0,1000000)
    if skontroluj_id_duplicitu(id) is False:
        return id

def skontroluj_id_duplicitu(id: int):
    """
    Funkcia kontroluje ci existuje duplicita medzi id cislami v databaze
    :param id:  cislo od 0 do 1000000
    :return:  Boolean hodnota ak je duplicita True ak nie je False
    """
    for i in baza_dat.values():
        if id in baza_dat[i][0]:  # ked je True
            print("DUPLICITA")
            return True
    print("DUPLICITA NEJESTVUJE")
    return False

def basic_view():
    """
    Zakladny vypis z databazy aby sme vedeli jej obsah
    :return:  Nevracia nic - TODO neskor moze vraciat status
    """
    for i in baza_dat.keys():
        print(i, baza_dat[i][0], baza_dat[i][3] )
    return

def nova_karticka():
    """

    :return:
    """
    print("ZADAJ NOVU KARTICKU DO SYSTEMU ZETTELKASTEN")
    nazov_karticky = input("NAZOV KARTICKY")  # TODO Dorobit aby nebola prazdna karticka
    id_cislo = generuj_id()
    linky = list()  # TODO DOrobit funkciu na pridavanie linkov
    tagy = list() # TODO Dorobit funkciu na pridavanie tagov
    obsah_karticky = input("TEXT KARTICKY")
    baza_dat[nazov_karticky] = [id_cislo, linky, tagy, obsah_karticky]  # Tu sa uklada nova karticka do Slovnika


while True:
    """ HLAVNY PROGRAM, KTORY POMOCOU NEKONECNEHO CYKLU PRIJIMA PRIKAZY OD UZIVATELA"""
    cmd = input("ZADAJ PRIKAZ q-quit|n-new|v-view")  # vstup z klavesnice uzivatela
    if cmd == "q":  # ak je command q -> ukonci program
        break
    elif cmd == "n":  # ak je command n -> vytvor novu karticku
        nova_karticka()  # vola funkciu nova karticka
    elif cmd == "v":  # ak je prikaz v -> zobraz zakladny vypis z dayabazy
        basic_view()  # vola funkciu zakladny vypis





