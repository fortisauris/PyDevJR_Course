chladnicka = dict()  # vytvorime si slovnik chladnicka
chladnicka["dvere"] = ["maslo", "mlieko", "juice", "syr"]  # vlozime klucove slovo dvere a zoznam potravin
chladnicka["aktualna teplota"] = 7.3  # vlozime klucove slovo aktualna teplota a hodnotu typu float

print(chladnicka)  # vypiseme chladnicku do konzoly

print(chladnicka.keys())  # pouzijeme metodu keys aby nam vypisala vsetky klucove slova
print(chladnicka["aktualna teplota"])  # vypiseme aktualnu teplotu
print(chladnicka.get("aktualna teplota"))  # vypiseme aktualnu teplotu pomocou metody get

b = dict()  # vytvorime si prazdny slovnik
b["aktualna teplota"] = 7.0  # vlozime don klucove slovo a hodnotu typu float
chladnicka.update(b)  # aktualizujeme slovnik chladnicka hodnotami zo slovnika b pomocou metody update
print(chladnicka.get("aktualna teplota"))  # opat vypiseme hodnotu aktualnej teploty v chladnicke

# TODO Spravte v Pythone jednoduchy program kde bude 1 cyklus, dve premenne a aspon jedna logicka podmienka.

chladnicka["policka1"] = ["salama", 'sunka', 'zeler']  # pouzijeme slovnik chladnicka a vytvorime klucove slovo policka
chladnicka["policka2"] = ["zemiaky", 'kecup', 'zeler']

def vypis_policku(chladnicka: dict, cislo_policky: str):  # vytvorime jednoduchu FUNKCIU a
    """
    Tato nasa funkcia nam vypise obsah policky
    :param chladnicka: Slovnik z ktoreho chceme vypisovat
    :param cislo_policky:  klucove slovo policky
    :return: obsah policky v nasom pripade zoznam
    """
    return chladnicka[cislo_policky]

def zrataj(a, b):  # funkcia je nas dalsi prikaz pythonu
    """
    Jednoducha funkcia na zratanie dvoch parametrov
    :param a: cislo, string, bool
    :param b: cislo, string, bool
    :return: vysledok suctu
    """
    print(a + b)  # kontrolny print do konzoly
    return a + b  # funkcia (podprogram ) vrati hodnotu suctu

#  Konvencia PYTHONU
# Najprv importy
# Potom Classy a funkcie
# potom kod hlavneho programu


obsah_policky = vypis_policku(chladnicka=chladnicka, cislo_policky="policka1")  # volame funkciu vypis policku
print(obsah_policky)  # vypiseme to co funkcia vratilo ulozene v premennej obsah_policky
print(zrataj(43254,67476))  # volame funkciu zrataj

'''
KOD KTORYM ZACINAME HLAVNY PROGRAM 

if __name__ == "__main__":
    # kod
'''

# funkcia odrataj
def odrataj(a, b):
    '''
    tato funkcia odratava dve cisla. pozor vstupy treba verifikovat aby nevznikali bugy. Vstupom funkcie
    nesmu byt Stringy
    :param a: cislo
    :param b: cislo
    :return: vysledok odcitania
    '''

    print(a - b)
    return a -b

# funkcia nasob
# funkcia delenie

zrataj(432, 5435)  # volame funkciu zrataj a ako parametre davame cisla
zrataj("Ahoj", " Svet") # volame funkciu zrataj a ako parametre davame stringy
odrataj(43, 65) # volame funkciu odrataj a ako parametre davame cisla
# odrataj("Ahoj", "Svet")  # ak zadame text tak vyhodi chybu


class NasaTrieda(object):
    '''
    Datova trieda obsahujuca data o nasom kurze. Samotna konstrukcia triedy je len planik toho
    ako bude skutocna trieda vyzerat. Vznikne az ked vytvorime objekt jej typu
    '''

    def __init__(self):
        """
        metoda init hovori ake premenne a aky kod sa ma vykonat pri iniacializacii OZIVENI triedy
        """
        self.menny_zoznam = list()  # premenna triedy
        self.pocet_hodin = int()  # premenna triedy
        self.nazov_kurzu = str()  # premenna triedy

    def pocet_ziakov(self):
        """
        Metoda triedy vypise pocet ziakov v kurze
        :return:  vrati dlzku menneho zoznamu
        """
        return len(self.menny_zoznam)

    def vypis_zoznam(self):
        """
        Metoda triedy vypise zoznam ziakov pod seba
        :return:  nic
        """
        for i in self.menny_zoznam:  # cyklus for prejde vsetky polozky v mennom zozname a vypise ich pod seba
            print(i)

    def je_ziak_clenom_kurzu(self, meno: str):
        """
        Metoda triedy vypise Bool ci sa meno nachadza na zozname
        :param meno: string
        :return: Bool
        """
        return meno in self.menny_zoznam  # hlada meno v zozname a vrati hodnotu True alebo False


obj = NasaTrieda()  # TU AZ VZNIKOL OBJEKT NasaTrieda
print(obj.__repr__())  # potvrdi ze objekt jestvuje a nachadza sa v pamati... ide o tzv. Magicku metodu.
obj.menny_zoznam = ["Michal", "Andrej", "Jan"]  # vkladame hodnoty do premennej triedy
print(obj.menny_zoznam)  # vypiseme zoznam ziakov
print(obj.pocet_ziakov())  # pouzijeme metodu objektu a zistime pocet ziakov
print(obj.vypis_zoznam())  # nechame vypisat ziakov pod seba

print(obj.je_ziak_clenom_kurzu("Jozef"))  # zistujeme ci ziak Jozef je ziakom kurzu
print(obj.je_ziak_clenom_kurzu("Andrej"))  # zistujeme ci ziak Andrej je ziakom kurzu
obj.pocet_hodin = 160  # nastavujeme hodnotu pocet hodin -
print(obj.pocet_hodin)  # nechame ju vypisat

class Ryba(object):
    """
    trieda Ryba nam ukazuje jednoduchy model ryby
    """

    def __init__(self, latinsky_nazov: str, voda: str):  # premenne v tejto zatvorke vyzaduje trieda pri inicializacii
        self.nazov = latinsky_nazov  # string
        self.voda = voda  # vkladame udaj ci ide o rybu sladkovodnu ci morsku

    def plava(self):
        """
        Jednoducha metoda triefy, ktora umoznuje nasej rybe plavat ked ju zavolame. Vyuzijeme cyklus for
        aby plavala 5x za sebou
        :return: None - Nic
        """
        for i in range(0,5):
            print("PLAVA")





ryba1 = Ryba(latinsky_nazov="Cyprinus carpio", voda="sladkovodna")  # Inicializujeme objekt triedy RYBA
print(ryba1.nazov)  # vypisujeme udaj z triedy
print(ryba1.voda)  # vypisujeme ci je sladkovodna ci morska
ryba1.plava() # nechame ju plavat


class Flasa(object):
    """
    Trieda je zjednodusenym modelom objektu Flasa a kopiruje jeho fyzicky model.
    """

    def __init__(self, objem, obsah):  # hodnoty objem a obsah vyzadujeme pri inicializacii objektu
        self.farba = "zelena"  # nastavujeme DEFAULTNU hodnotu na zelena
        self.objem = objem  # premenna triedy v mililitroch
        self.obsah = obsah  # premenna triedy
        self.naplnenost = 0  # naplnenost v mililitroch DEFAULTNE prazdna

    def vylievanie(self, odlej: int):
        """
        Jednoducha metoda na vylievanie z flase
        :param odlej: kolko mililitrov chceme odliat
        :return: Netreba. premenne triedy sa aktualizuju aj bez returnu
        """
        if self.naplnenost > odlej:  # kontrolujeme ci je vo flasi dostatok tekutin na odliatie
            self.naplnenost -= odlej  # odlievame

        else:
            print("FLASA NEOBSAHUJE DOSTATOK TEKUTINY")  # ak flasa neobsahuje dostatok tekutiny tak vypise :



obj = Flasa(objem=1000, obsah="voda")  # tu vznika objekt Flasa
obj.farba = "modra"  # menime farbu objektu na modra
print(obj.farba)  # kontrolujeme zmenu v premennej objektu
obj.vylievanie(150)  # odlievame 150 ml

print("PREDTYM",obj.__repr__())  # kontolujeme objekt v pamati
del obj  # zahodime / znicime objekt Flasa
print("POTOM",obj.__repr__())  # Objekt uz neexistuje

# TODO Vytvorit classu a inicializovat vznik objektu.
# chcem vytvorit metodu, ktora mi povie ake skupenstvo ma obsah flase








