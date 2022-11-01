abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def xor_dec(enc_msg: list, heslo: str):
    """
    Funkcia decryptuje pomocou funkcie XOR a hesla spravu, ktora bola zasifrovana do cisel.
    :param enc_msg: zoznam cisel - zasifrovana sprava list
    :param heslo: heslo String
    :return: Desifrovana sprava string
    """
    dec_msg = ""  # prazdny string
    prepared_heslo = (100 * heslo)[:len(enc_msg)]
    for i in range(0,len(enc_msg)):
        # print("ENC_znak", enc_msg[i], "ZNAK v ABECEDE: ", abeceda.index(prepared_heslo[i]))
        dec_znak = enc_msg[i] ^ abeceda.index(prepared_heslo[i])  #
        # print(dec_znak, abeceda[dec_znak])
        dec_msg += abeceda[dec_znak]
    return dec_msg



# Interpretovany alebo Kompilovany ?  Interpretovany
# Vysokourovnovy jazyk,
# Objekto-orientovany

# Interaktivna konzola
# pouzite skriptu, ktory spustime cez terminal

#  P R O G R A M  N A   S K U S A N I E   O T A Z O K
# Program na testovanie otazok a,b,c

# Otazky si dame do Slovnika dict()  {"Otazka": ["a - Odpoved1", "b-Odpoved2", "c - Odpoved3", "c"]}

# Nekonecny cyklus  while True:

# Otazky budeme vyberat pomocou random.choice()

# odpovedat budeme pomocou prikazu input()

# vyhodnotime spravne odpovede

a = 65436
print(type(a))
print(dir(a))
print(abs(a))
print(a.bit_length())
print(a.to_bytes(2, byteorder="little"))
print(a.__hash__())

a = "Hello World"
print(type(a))
print(a.capitalize())
print(a.casefold())  # agresivnejsie capitalize
print(a.center(24, "_"))
print(a.count("l"))
print(a.encode(encoding="utf8", errors="strict"))
print(a.endswith(("d","o"), 0, 5))
print(a+"\tDobre\t".expandtabs(tabsize=4))
print(a.find("llo", 0, len(a)))  # nevyhodi chybu

print("Hello", "World", "Ako sa Mas ?")

# F O R M A T O V A N I E   T E X T U

a = "Toto je udaj {0} vlozeny formatovanim textu {1}"
print(a.format("HODNOTA0", "HODNOTA1"))

print(a.index("udaj", 0, len(a)))  # vyhodi chybu

print("alpha5435".isalnum())
print("Andrej54356".isalpha())
print(a.isascii())
print("54343hello".isdecimal())
print("43".isdigit())
print("Az_4535".isidentifier())
print("4343fhdjshf!!".isidentifier())

print("Az_4535".islower())
print("Az_4535".isnumeric())
print("Az_4535".isprintable())
print("Az_4535".isspace())

a = "Hello"
print(a.join(" WOrld"))
print(a.lstrip("H"))
print(a.removeprefix("H"))
print(a.removesuffix("o"))
print(a.swapcase())
print(a.replace("H", "A"))
print("4535".zfill(8))

'''
P O K R O C I L E   F O R M A T O V A N I E   T E X T U
'''

print("Tento %(jazyk)s je uradny jazyk pre %(obyvatelov)05d na Mauriciu." %
      {"jazyk": "Francuzsky", "obyvatelov": 5435})
print(f"Tento %(jazyk)s je uradny jazyk pre %(obyvatelov)05d na Mauriciu." %
      {"jazyk": "Francuzsky", "obyvatelov": 5435})

'''
Modul csv - Comma Separated Variables
'''
import csv

a = [12, True, "Jolana", 5453.543]
b = [143, False, "Artur", 17.30]

# ZAPISAL DO CSV SUBORU
with open("data.csv", mode="w", newline="") as csvfile:
    datawriter = csv.writer(csvfile, dialect='excel', delimiter=" ")
    datawriter.writerow(a)
    datawriter.writerow(b)

# NACITAL Z CSV SUBORU
with open("data.csv", mode='r', newline="") as csvfile:
    datareader = csv.reader(csvfile, delimiter=" ")
    for riadok in datareader:
        print(riadok)

with open("names.csv", mode="w", newline="") as csvfile:
    fieldnames = ["meno", 'priezvisko']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"meno": "Jozef", "priezvisko": "Mrkvicka"})
    writer.writerow({"meno": "Bohuslav", "priezvisko": "Kovac"})
    writer.writerow({"meno": "Roman", "priezvisko": "Kristof"})

with open("names.csv", mode="r", newline="") as csvfile:
    datareader = csv.DictReader(csvfile)
    for riadok in datareader:
        print(riadok['meno'], riadok['priezvisko'])

print(csv.list_dialects())


def collatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n /2
        else:
            n = 3 * n + 1

collatz(29)
import os

def Vernam_enc(sprava: str):
    """
    Vernamova skoro nerozlusknutelna sifra pouziva funkciu XOR spolu s nahodnymi cislami s vysokou
    entropiou. Nam ju zabezpeci modul os metodou urandom, ktory vyuziva kryptograficky silny generator
    v TPM chipe Vaseho pocitaca.
    TPM je kryptograficky chip na generovanie a uchovavanie kryptografickych klucov.
    :param sprava: textova sprava String
    :return: ciselne hodnoty zasifrovanej spravy list
    """
    kluc = os.urandom(len(sprava))
    preparovany_kluc = list()
    enc_sprava = []
    for i in kluc:
        preparovany_kluc.append(i)
    print(kluc, preparovany_kluc)
    for i in range(0, len(sprava)):
        enc_znak = abeceda.index(sprava[i]) ^ preparovany_kluc[i]
        print(enc_znak)
        enc_sprava.append(enc_znak)
    return enc_sprava

print(Vernam_enc("BRYNDZAZDRAZELA"))

# TODO Spravit Vernam_decrypt

# TODO Prestavka do 20:15


'''
ZETELLKASTEN system
'''
import random

baza_dat = dict()  # tu budu vsetky nase data  SLOVNIK

def generuj_id():
    """
    Funkcia nam generuje id cislo karticky. Pomocou odkazov na id cislo vieme prepajat karticky
    s poznatkami
    :return:
    """
    id = random.randint(0, 1000000)
    if skontroluj_id_duplicitu(id) is False:
        return str(id).zfill(6)
    return


def skontroluj_id_duplicitu(id: int):
    """
    Funkcia kontroluje ci existuje duplicita medzi id cislami v databaze
    :param id:  cislo od 0 do 1000000
    :return:  Boolean hodnota ak je duplicita True ak nie je False
    """
    for i in baza_dat.keys():
        if id in baza_dat[i][0]:  # ked je True  # TODO Skontrolovat TypeError unhashable type list
            print("DUPLICITA")
            return True
        else:
            print("DUPLICITA NEJESTVUJE")
            return False

def basic_view():
    """
    Zakladny vypis z databazy aby sme vedeli jej obsah
    :return:  Nevracia nic - TODO neskor moze vraciat status
    """
    for i in baza_dat.keys():
        print(i, baza_dat[i][0], baza_dat[i][1],  baza_dat[i][2], baza_dat[i][3] )
    return

def nova_karticka():
    """
    Funkcia pomocou ktorej definujeme novu karticku
    :return:
    """
    print("ZADAJ NOVU KARTICKU DO SYSTEMU ZETTELKASTEN")
    nazov_karticky = input("NAZOV KARTICKY")
    skontroluj_nazov_karticky(nazov_karticky)
    id_cislo = generuj_id()
    linky = zadaj_linky()  # Tu volame funkciu na zadanie liniek na karticku
    tagy = zadaj_tagy()  # Tu volame funkciu na zadavanie tagov na karticku
    obsah_karticky = input("TEXT KARTICKY")
    baza_dat[nazov_karticky] = [id_cislo, linky, tagy, obsah_karticky]  # Tu sa uklada nova karticka do Slovnika


def skontroluj_nazov_karticky(nazov):
    if nazov == "":
        print("NEVYHOVUJUCI NAZOV KARTICKY")
        nova_karticka()

def zadaj_linky():  # [[id]]
    result = list()
    while True:
        command = input("ZADAJ LINKU ALEBO q PRE UKONCENIE")
        if command == "q":
            break
        else:
            prepare_link = "[[ " + command + " ]]"
            print(prepare_link)
            result.append(prepare_link)
        # TODO Sprav funkciu, ktora bude vyberat z existujucich karticiek
    print(result)
    return result

def zadaj_tagy():  # [[id]]
    result = list()
    while True:
        command = input("ZADAJ TAG ALEBO q PRE UKONCENIE")
        if command == "q":
            break
        else:
            prepare_link = "#" + command + " "
            print(prepare_link)
            result.append(prepare_link)
        # TODO Sprav funkciu, ktora bude vyberat z existujucich karticiek
    print(result)
    return result

while True:
    """ HLAVNY PROGRAM, KTORY POMOCOU NEKONECNEHO CYKLU PRIJIMA PRIKAZY OD UZIVATELA"""
    cmd = input("ZADAJ PRIKAZ q-quit|n-new|v-view")  # vstup z klavesnice uzivatela
    if cmd == "q":  # ak je command q -> ukonci program
        break
    elif cmd == "n":  # ak je command n -> vytvor novu karticku
        nova_karticka()  # vola funkciu nova karticka
    elif cmd == "v":  # ak je prikaz v -> zobraz zakladny vypis z dayabazy
        basic_view()  # vola funkciu zakladny vypis





