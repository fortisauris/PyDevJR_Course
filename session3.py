'''
SESSION 3 - TRIEDY, SNIPPET, ZACHYTAVANIE CHYB, MODULY TIME, OS, SYS, RANDOM,  RE, HASHLIB, sifra SCYTALE


TRIEDA TEPLOMER

DEDICNOST TRIED - TRIEDA Rodic(), Trieda Dieta()

SNIPPET je cast kodu, ktoru mozeme potom pouzit vo vsetkych svojich programoch

SNIPPET - TRIEDA FileTools()

ZACHYTAVANIE CHYB V PYTHONE (try:except:finally:)

ZAKLADNE MODULY time, os, sys, re, hashlib

K R Y P T O G R A F I A. - SCYTALE

L A M B D A  F U N K C I E 
'''

''' IMPORTY '''

import random
import time
import re
import sys
import os
import hashlib


'''FUNKCIE A TRIEDY'''

'''TRIEDA. Teplomer()'''
class Teplomer(object):
    """
    Trieda teplomer je jednoducha trieda na uchovavanie teploty

    """

    def __init__(self):
        self.teplota = 21

    def get_teplota(self):
        return self.teplota

    def set_teplota(self, stupne_celsia: float):
        self.teplota = stupne_celsia


'''TRIEDA. Rodic()'''
class Rodic(object):  # Rodicovska trieda
    '''
    Trieda Rodic je jednoducha trieda na demonstraciu dedicnosti tried. Ma nastavenu iba jednu
    premennu triedy a to temperament. 
    '''
    def __init__(self):
        '''
        Magicka metoda, ktora nam pri iniciacii triedy Rodic vykona svoj kod
        '''
        self.temperament = 'cholerik'
        print("SOM CHOLERIK")  # tento kod sa vykona pri inicializacii

    def get_temperament(self):  # metoda Getter, ktoru preberie Dieta
        '''
        Metoda triedy rodic, ktora nam na zavolanie vrati temperament Rodica
        '''
        return self.temperament

'''TRIEDA. Dieta()'''
class Dieta(Rodic):  # Triedy po ktorych Dieta dedi moze byt viac

    def __init__(self):
        '''
        Magicka metoda, ktora nam pri iniciacii triedy Rodic vykona svoj kod
        '''
        super().__init__()  # explicitne zadavame aby zdedil aj __init__() rodica

        
''' TRIEDA FileTools - demonstracia statickych a klass metod '''
class FileTools(object):
    """
    Triedy nemusia byt len datove, mozu obsahovat ak je to opodstatnene programy, ktore mozeme
    vyuzit aj bez inicializacie triedy FileTools - to znamena ze objekt nevznikne

    """
    @staticmethod  # decorator je funkcia ktora modifikuje nasu funkciu, v tomto pripade hovori pythonu ze je nezavisla
    def file_save(filename_w_path: str, plaintext :str):  # NEDAVAME TAM self !!!
        f = open(file=filename_w_path, mode="w", encoding="utf8")  # pomocou prikazu otvarame subor na zapisovanie
        f.write(plaintext)  # zapisujeme text do suboru
        print("SUBOR SA ULOZIL")  # vypiseme stav do konzoly
        f.close()  # uzatvarame subor

    @classmethod
    def file_load(cls, filename_w_path: str):
        f = open(file=filename_w_path, mode="r", encoding="utf8")  # mode r znamena READ otvarame subor na citanie
        nacitany_text = f.read()
        print(nacitany_text)
        f.close()
        return nacitany_text  # vraciame nacitany test pre dalsie pouzitie

    
'''
K R Y P T O G R A F I A. SCYTALE
Historicky algoritmus na jednoduche zasifrovanie obsahu stary tisicky rokov
Recept : potrebujeme 2 rovnako hrube palice 
                    potrebujeme pasik koza

Nacelnik omotal kozu okolo palice, napisal spravu pod seba  a potom doplnil medzeru nahodnymi pismenami.
'''
def scytale_enc(text : str, hrubku_palice: int):  # definujeme funkciu
    zasifrovana_sprava = ""  # vytvarame prazdny vysledok sifrovania
    for i in text:  # pomocou cyklu ideme cez text, ktory chceme zasifrovat
        zasifrovana_sprava += i  # pridavame pismenko do retazca
        for k in range(0, hrubku_palice):  # pomocou cyklu budeme pridavat urcity pocet nahodnych znakov podla hrubky palice
            nahodny_znak = random.choice("ABCDEFGHIJKLMNOPGRSTUVWXYZ")  # vyberame nahodny znak z abecedy
            zasifrovana_sprava += nahodny_znak  # pridavame nahodny znak k sprave
    return zasifrovana_sprava  # vraciame zasifrovanu spravu



    
''' FUNKCIA hash_it() '''
def hash_it(text: str):  # jednoducha funkcia na vypocet hashstringu zo zadaneho textu HESLA
    '''
    Jednoducha funkcia na vypocitanie hashu z nejakych dat. Hash je nieco ako digitalny odtlacok prsta dat.
    Aj mala zmena v datach znamena velku zmenu vo vysledku. Preto ak sa dve hashe zhoduju mozeme tvrdit ze vstupne
    data boli rovnake.  
    
    ALGORITMY SHA1 a MD5 UZ NIE SU KRYPTOGRAFICKY BEZPECNE !!!
    
    param1::: text - String
    return::: hexdigest - hexadecimalny retazec vysledku algoritmu
    '''
    h = hashlib.md5()  # vytvorenie objektu hashovacieho algoritmu
    data = bytes(text, encoding="utf8")  # pripravime si data - konverzia na bytes
    h.update(data)  # hadzeme vsetko do mixera
    return h.hexdigest()  # vrati nam hexadecimalny kod podla vybraneho algoritmu

'''    H L A V N Y   P R O G R A M   '''
if __name__ == '__main__':
    '''MANIPULACIA S TRIEDOU. Teplomer()'''
    teplomer_v_obyvacke = Teplomer()  # inicializacia triedy
    teplomer_v_obyvacke.teplota = 27  #  nastavi hodnotu teplomera
    print(teplomer_v_obyvacke.teplota)  # vypise hodnotu teplomera
    teplomer_v_obyvacke.set_teplota(22.3)  # pomocou metody Setter nastavime novu hodnotu
    print(teplomer_v_obyvacke.get_teplota())  # pomocou metody Getter vypiseme hodnotu

    # TODO Spravte novu premennu triedy a setter k nej


    ''' MANIPULACIA S TRIEDOU. Dieta()  '''
    obj = Dieta()  # inicializujeme triedu

    '''
    SNIPPET je cast kodu, ktoru mozeme potom pouzit vo vsetkych svojich programoch

    TRIEDA FileTools() - obsahuje staticke a class metody, ktore mozeme zavolat aj bez inicializacie triedy

    STATICKE A CLASS METHODY NESMU POUZIVAT PREMENNE TRIEDY TYPU self.premenna
    '''


    ''' MANIPULACIA S METODAMI FileTools()'''
    FileTools.file_save(filename_w_path="skuska.txt", plaintext="Dnes pokracujeme v pisani programov.")
    FileTools.file_load(filename_w_path="skuska.txt")


    '''MODUL random '''
    print(random.random())  # generuje cislo od 0 do 1
    print(random.randint(0, 10000))  # generuje cislo od 0 do 10000
    a = random.choice(["Andrej", "Jan", "Filip", "Rebeka"])  # vyberie z obsahu zatvorky nahodnu hodnotu
    print(a)
    print(random.randbytes(256))  # vygeneruje nahodnych 256 bytov v hexadecimalnom kode


    '''MODUL time'''
    print(time.time())  # vytlaci systemovy cas ... od 1.1.1970
    cas = time.localtime()  # vytlaci objekt obsahujuci udaje o datume a case
    print(cas[0:6])  # da sa KRAJAT
    nas_cas = str(cas[0:6])  # skonvertujeme ho na String
    FileTools.file_save(filename_w_path="nas_cas.txt", plaintext=nas_cas)  # ulozime ho do naseho suboru
    print(time.strftime("%H:%M:%S"))  # vytlaci cas v predefinovanom formate

    ''' ZACHYTAVANIE CHYB V PYTHONE (try:except:finally:)'''

    try:  # vyskusaj
        vysledok = 34 / 0  # tu vyhodi chybu
    except ZeroDivisionError:  # tu ju zachytime
        print("NEDA SA DELIT NULOU")  #
        vysledok = 34 / 1  # tu ju opravime
    finally:
        pass  # nerob nic kasli na to

    # TODO Program sifrovanie Scytale

    ''' K R Y P T O G R A F I A. SCYTALE. - MANIPULACIA S FUNKCIU scytale_enc() '''
    sprava_pre_nacelnika = "BRYNDZAZDRAZELA"  # sprava na zasifrovanie
    enc = scytale_enc(text=sprava_pre_nacelnika, hrubku_palice=6)  # pouzitie funkcie
    print(enc)

    # TODO DOmaca uloha decryptovat nasu spravu  HINT zobrazte kazde sieste pismeno
    # BZVFOLPRSGYMWIYOVGLBBNZUUZNSDNEOESOZFXELCOAPNCGOWZOWVFOPDXDFCGKRKVPWLZAOZIARFZVGYGGYEWJCBOCLKNGRCGAVJLHTH

    '''
    M O D U L  re (REGULAR EXPRESSIONS)- mocny nastroj na vyhladavanie v texte
    '''

    text = "Toto som nasiel o 18:00 som pred som domom."

    print(re.findall(pattern="som", string=text))  # najde pocet hladanych stringov a vlozi do zoznamu

    print(re.search(pattern="Toto", string=text))

    print(re.match(pattern="Toto", string=text))  # hlada zhodu medzi stringami
    print(re.match(pattern=text, string=text))

    print(re.fullmatch(pattern="Toto", string=text))  # hlada uplnu zhodu medzi stringami
    print(re.fullmatch(pattern="Toto", string=text[0:4]))

    a = re.search(pattern="Toto", string=text)  # vytvoreny objekt re.match vieme potom rozobrat
    print(a)
    print(a.group())
    print(a.span())

    '''
    REGULAR EXPRESSIONS GENERATORY vedia pomoct ked hladate v texte nieco specificke
    '''


    # PRESTAVKA DO 20:05

    '''
    Modul SYS zistuje informacie o pocitaci a systeme
    '''

    print(sys.platform)
    print(sys.version_info)
    print(sys.modules.keys())
    print(sys.path)

    print(sys.argv)  # nasledujuce riadky budu fungovat iba pri spustani cez terminal
    # TODO vyskusat spustat skripty cez Terminal s argumentami :
    #  python.exe ./session3.py 543 6546
    # a = eval(sys.argv[1])  # prikazom eval menime string na cislo... pozor musime ho validovat
    # b = eval(sys.argv[2])
    # print(a + b)

    '''
    MODUL OS
    '''
    os.system("dir")  # vykona obsah zatvorky v Terminali
    print(os.listdir())  # DIR vrati list
    print(os.getcwd())  # GET CURRENT DIRECTORY
    info = os.walk(top="C:")
    print(info)
    print(list(info))

    '''
    MODUL HASHLIB
    '''

    ''' MANIPULACIA S FUNKCIU hash_it() '''
    print(hash_it("anna1978"))  # luskanie hesla max 5znakov cisla # tu volame funkciu hash_it


    # TODO Spravit Bruteforce luskanie hesla  821e060b573688ae584b2c1ece04dfe6
    # TODO Pouzite cyklus for a vypocitajte vsetky hashe od 10000 do 99999
    # TODO nezabudnite cislo skonvertovat na string pomocou str()
    # TODO Pomocou logickeho bloku if porovnavajte vypocitany hash z hashom skopirovanym z 196teho riadku.
    # TODO Ak je zhoda tak vypiste cislo

    '''     L A M B D A. FUNKCIE    '''
    # def sucet(x,y):  # klasicky format funkcie
    #    return x + y

    # print(sucet(10,10)) # vysledok bude 20

    vysledok = lambda x, y: x + y  # lambda funkcia, zjednodusena forma

    print(vysledok(10, 10))













