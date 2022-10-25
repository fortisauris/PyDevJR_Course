'''
ZAKLADNY SYNTAX PYTHONU
'''

# print
# Premenna
# len - dlzka
# input
# Cyklus for a while
# Logicke bloky  if else
# Funkcie  def a Anonymne funkcie lambda
# Triedy  class
# Moduly  time, random, sys, os, re, hashlib
# quit()
# pass
import random
import time


# vytvor cyklus od 10 do 32

class FileTools(object):  # Novy nastroj vo FileTools
    """
    Triedy nemusia byt len datove, mozu obsahovat ak je to opodstatnene programy, ktore mozeme
    vyuzit aj bez inicializacie triedy FileTools - to znamena ze objekt nevznikne

    """
    @staticmethod  # decorator je funkcia ktora modifikuje nasu funkciu, v tomto pripade hovori pythonu ze je nezavisla
    def file_save(filename_w_path: str, plaintext :str):  # NEDAVAME TAM self !!!
        """
        Metoda triedy uklada STRING do zadaneho suboru
        :param filename_w_path: nazov suboru s cestickou : String
        :param plaintext: text na zapisanie do suboru : String
        :return: None
        """
        f = open(file=filename_w_path, mode="w", encoding="utf8")  # pomocou prikazu otvarame subor na zapisovanie
        f.write(plaintext)  # zapisujeme text do suboru
        print("SUBOR SA ULOZIL")  # vypiseme stav do konzoly
        f.close()  # uzatvarame subor

    @classmethod
    def file_load(cls, filename_w_path: str):
        """
        Metoda cita text zo suboru
        :param filename_w_path: nazov suboru s cestickou : String
        :return: nacitany text : String
        """
        f = open(file=filename_w_path, mode="r", encoding="utf8")  # mode r znamena READ otvarame subor na citanie
        nacitany_text = f.read()
        print(nacitany_text)
        f.close()
        return nacitany_text  # vraciame nacitany test pre dalsie pouzitie

    @classmethod
    def file_exist(cls, filename_w_path: str):
        """
        Metoda zistuje existenciu suboru pred nacitanim a vracia True ak jestvuje a False ak nejestvuje
        :param filename_w_path: nazov suboru s cestickou : String
        :return: Bool
        """
        try:  # vyskusaj
            f = open(file=filename_w_path, mode="r", encoding="utf8")  # otvara subor na citanie
            f.read()  # cita
        except FileNotFoundError:  # zachytava chybu
            return False  # vracia False ak subor neexistuje
        finally:  # ukoncenie bloku
            pass  # kasli na to
        return True  # vrati True ak chyba neprebehla a subor jestvuje

# PRIKLAD POUZITIA NASEHO NOVEHO NASTROJA
if FileTools.file_exist("halabala.txt") is True:
    FileTools.file_load("halabala.txt")
else:
    print("SUBOR NEEXISTUJE")

#  Spravime premennu pocitadlo
# nastavime na nulu
# spustime nekonecny cyklus
# logicky blok ak pocitadlo je viac ako 10 - > napis do konzoly "DONE" a pouzi break na ukoncenie cyklu
# pripocitaj k pocitadlu jednotku


# CAESAROVA SIFRA

# ABCDEFGH
# spravime funkciu na posunutu abecedu
# premenna abeceda STRING "ABC..."


abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # definujeme abecedu pre nas algoritmus

def posunuta_abeceda(posun: int):
    """
    Funkcia upravi abecedu pomocou posunu pismen o urcenu hodnotu
    :param posun: cislo o ktore posunie abecedu doprava alebo dolava: Integer
    :return: posunuta abeceda : String
    """
    return abeceda[posun:] + abeceda[:posun]

def caesar_enc(text: str, posun: int):
    """
    Funkcia zasifruje text pomocou Ceasarovej sifry (jednoduchy posun)
    :param text:  sprava na zasifrovanie : String
    :param posun: posunutie abecedy: Integer
    :return: zasifrovana sprava : String
    """
    posunuta = posunuta_abeceda(posun)  # pouzijeme funkciu posunuta abeceda
    enc_text = ""  # definujeme premennu kde sa bude ukladat zasifrovany text
    for i in text:  # pomocou cyklu for prechadzame cyklom
        if i == " ":  # ak je znakom medzera tak
            enc_text += " "  # vloz do zasifrovaneho textu medzeru
        else:
            symbol_pozicia = int(abeceda.index(i))  # ak je iny znak zisti jeho polohu v abecede
            enc_text += posunuta[symbol_pozicia]  # pridaj znak posunutej abecedy s indexom normalnej abecedy
    return enc_text.upper()  # vrat zvacseny text

print(caesar_enc("AHOJTE VSETCI A VELA USPECHOV V PROGRAMOVANI", 3))

#TODO Funkciu na desifrovanie

import pickle
import random
import time
import hashlib

obj = ["Andrej", 3245, True, [54,76,878,465,0]]  # cvicny zoznam


class Auto(object):  # cvicna trieda

    def __init__(self):
        self.farba = "biela"
        self.palivo = "diesel"

    def motor(self):
        return "BRM BRM"



zavarina = pickle.dumps(obj)  # zavarili sme zoznam do pamati
print(zavarina)  # vytlacime si ho, alebo ho mozeme niekam vlozit v podobe bytov

auto = Auto()  # inicializujeme triedu Auto
zavarina2 = pickle.dumps(auto)  # Zavarujeme si auto
print(zavarina2)  # tlacime si to do konzoly

print(pickle.loads(zavarina))  # otvarame zavaraninu a vracia sa objekt
print(pickle.loads(zavarina2))  # otvarame zavaraninu a vracia sa objekt
auto2 = pickle.loads(zavarina2)  # ukladame otvorenu zavaraninu do premennej auto


with open(file="zavaranina.obj", mode="wb") as f:  # pythonisticky sposob otvarania suborov v binarnom zapisovani
    pickle.dump(obj=auto, file=f)  # ukladame objekt do suboru

with open(file="zavaranina.obj", mode="rb") as f:  # pythonisticky sposob otvarania suborov v binarnom citani
    result = pickle.load(file=f)  # nacitavame objekt zo suboru

print(result)  # tlacime vysledok

def text():  #  funkcia
    """
    Toto je dokumentacia tejto funkcie
    :return: Nist
    """
    return "COKOLVEK"

print(text.__doc__)  # prezerame doctring funkcie


# TODO Skuste si zavarit nejaky objekt do suboru alebo len do pamati.

# PAUZA DO 19:50

'''
Algoritmus na pohovor - Fibonacciho rad cisel.
'''


def fibonacci(n):
    if n < 0:  # ak je n mensie ako nula ->
        print("Nespravny vstup")  # napis ze nespravny vstup

    elif n == 0: # ak sa rovna 0
        return 0  # vrat 0

    elif n == 1 or n == 2:  # ak sa rovna 1 alebo 2 ->
        return 1  # vrat 1
    else:  # inak ->
        return fibonacci(n-1) + fibonacci(n-2)  # pouzi rekurziu a tento matematicky vzorec


for i in range(0, 5):  # cyklus vypocita prvych 5 cisel Fibonacciho radu cisel
    print(fibonacci(i))  # vytlac vypocitane cislo


# Benchmark naseho PC a vykonnosti Pythonu pomocou modulov hashlib, time, random

# vytvorit zoznam a don vygenerovat 10000 nahodnych retazcov
def vzorka():  # vygenerujeme milion retazcov pre nas benchmark
    """
    Funkcia generuje MILION retazcov pre nas test
    :return: vysledok - retazce : List
    """
    vysledok = list()  # vytvorime zoznam kde ich budeme vkladat
    for _ in range(0, 1000000):  #
        retazec = str()  # definujeme prazdny retazec
        for k in range(0, 10):  # retazec bude dlhy 10 znakov
            retazec += random.choice(abeceda)  # pridavame nahodne vybrany znak z abecedy
        # print(retazec)  
        vysledok.append(retazec)  # pridavame retazec do zoznamu
    return vysledok  # vraciame vysledok

# print(vzorka())

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

# okopirovat funkciu hash_it z session3

t1 = time.time()  # START
vygenerovane_retazce = vzorka()  # generujeme retazce
for i in vygenerovane_retazce:  # prechadzame vzorkou ->
    hash_it(i)  # hashijeme kazdu hodnotu v zozname
t2 = time.time()  # KONIEC
print(t1, "\n\n", t2)  # tlacime vysledne casy do konzoly
total = t2-t1  # vypocitavame dlzku trvania
print(total)  # tlacime ju do konzoly


# vytvorit program, ktory postupne prejde cez zoznam a vypocita hashstringy
# TODO Odskusat na co najviac zariadeniach a porovnat vysledky
# merat cas

'''
Andrej 12.45   i3-7100
Filip 1.99  i7 - 12700
Viktor 9.82  i5 - ?? 
Baryalai 7.18 Ryzen3-1200
Jan 4.8 - Apple M1

'''





