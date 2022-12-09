'''
SESSION 12 - DEBUGGOVANIE A TESTOVANIE SOFTVERU

D E B U G G O V A N I E   S O F T V E R U
Pycharm - napravo od cisla riadku mozeme dat BREAKPOINT.
Potom pustime debuger a pomocou tlacitiek StepOver, StepInto a StepOut prechadzame kod.
Vsetky premmenne nam ukazuje pri kode ako sa menia

python.exe -m pdb ./session12.py

Spusta vstavany debugger priamo v Terminali.

help -- vsetky prikazy
ll - long list vypise program
b cislo_riadku - spravi breakpoint na riadku
c - pokracuj k dalsiemu breakpointu
p var1,var2,var3  - vypise aktualne hodnoty premennych
n - pokracuj na dalsi riadok
j cislo_riadku - skoc na riadok
q - quit debugger

T E S T O V A N I E   S O F T V E R U  - P Y T E S T

python.exe -m pytest -v testy.py

J E D N O D U C H Y  P I N G  pomocou urllib

M O D U L - JEDNODUCHY PORTSCANNER POMOCOU MODULU SOCKET

M O D U L - PRIPOJENIE NA POCITAC POMOCOU MODULU SOCKET

K R Y P T O G R A F I A - SBOX ENCRYPTION pre Stream Dat

A L G O R I T M U S  -  N A J K R A T S I A   C E S T A

'''
''' I M P O R T Y '''
import urllib.request, time
import random
import socket

# Texas existuje mestecko ktore sa vola Praha
# svojho casu mala Praha 150 obyvatelov
# priblizne 45% volicov bude volit Republikanov
# 47% percent volicov bude volit pravdepodobne Demokratov
# 8% volicov je este nerozhodnutych.

# nasimulujeme si nieco ?
# vytvorite Slovnik v ktorom bude 150 obyvatelov. Kluc bude str(1...150)
# republikanski_volici = 45% slovnika
# demokrati = 47% slovnika
# nerozhodnuti_volici = 8% pomocou random.choice(["Republikani", "Demokrati"])

# spocitate hlasy v slovniku.

# TODO Kto tu nie je tak domaca uloha :)

# Cambridge Analytica - Nerozhodni volici smerom k republikanom... pandas numpy jupyter notebook DATA ANALYST

''' F U N K C I E  A  C L A S S Y'''

'''
P R O G R A M   N A   D E B U G O V A N I E
Hadze ZeroDivisionError :) Debugujte 
'''

def urob_sucet(a,b):
    return a + b


def urob_delenie(a,b):
    #if b == 0:
    #    print("NEMOZES DELIT NULOU !!!")
    return a / 1
    #else:
    #    return a / b


def je_vysledok_cele_cislo(n):
    if n == int(n):
        return True
    else:
        return False
    
    
'''
T E S T O V A N I E   S O F T V E R U  - P Y T E S T
'''

# python.exe -m pip install pytest

def test_urob_sucet():
    assert urob_sucet(2,2) == 4
    assert urob_sucet(2,4) == 6
    assert urob_sucet("A", "HA") == "AHA"
    assert urob_sucet("A", str(6)) == "A6"

def test_urob_delenie():
    assert urob_delenie(10,0) == 10  # ZEro division
    assert urob_delenie(10,5) == 2

def test_cele_cislo():
    assert je_vysledok_cele_cislo(2.3) == False
    assert je_vysledok_cele_cislo(2) == True


'''
J E D N O D U C H Y  P I N G  pomocou urllib
'''


def ping_urllib(host):
    t1 = time.time()
    urllib.request.urlopen(host+"/index.html").read()  # toto nas asi spomaluje
    return ((time.time()-t1)*1000.0)
    

    
'''
JEDNODUCHY PORTSCANNER POMOCOU MODULU SOCKET
'''
    

def portscanner(ip4):
    vlajka = False
    porty_na_skenovanie = [21,22,80,447, 8000] # FTP, SSH, HTTP, HTTPS
    for port in porty_na_skenovanie:
        obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = obj.connect_ex((ip4,port))
        if result == 0:  # podarilo sa nadviazat spojenie
            print("ADRESA :", ip4, "PORT :", port, " JE AKTIVNY")
            vlajka = True
        else:
            pass
        obj.close()
    return True



'''
KRYPTOGRAFIA SBOX ENCRYPTION pre Stream Dat
'''

def sbox_enc(sbox, key):
    # pismeno bolo cislo od 0, 26
    key = ord(key)  # A v ASCII tabulke je 65
    enc_znak = int()
    for i in sbox:
        key ^= i
        # print(i, key)
    return key  # zasifrovane pismeno

'''
A L G O R I T M U S  -  N A J K R A T S I A   C E S T A
'''

def najkratsia_cesta(graph: dict, mesto1: str, mesto2: str):
    cesta_zoznam = [[mesto1]]
    cesta_index = 0

    predchadzajuce_mesto = {mesto1}
    if mesto1 == mesto2:
        return cesta_zoznam[0]

    while cesta_index < len(cesta_zoznam):
        aktualna_cesta = cesta_zoznam[cesta_index]
        posledne_mesto = aktualna_cesta[-1]
        dalsie_mesta = graph[posledne_mesto]

        if mesto2 in dalsie_mesta:
            aktualna_cesta.append(mesto2)
            return aktualna_cesta

        for dalsie_mesto in dalsie_mesta:
            if not dalsie_mesto in predchadzajuce_mesto:
                nova_cesta = aktualna_cesta[:]
                nova_cesta.append(dalsie_mesto)
                cesta_zoznam.append((nova_cesta))

                predchadzajuce_mesto.add(dalsie_mesto)
        cesta_index += 1
    return []


''' H L A V N Y.  P R O G R A M'''

if __name__ =='__main__': 
    for i in range(-5, 5):
        a = random.choice([3,5,7,9,11,13,23,45,67,89,100])
        b = i
        # sucet
        vysledok_suctu = urob_sucet(a,b)

        # delenie
        vysledok_delenia = urob_delenie(a,b)
        print(je_vysledok_cele_cislo(vysledok_delenia))
        print(a, b, vysledok_suctu,vysledok_delenia)

    # TODO Debugujte pomocou Debuggeru nejaky algoritmus


    # python.exe -m pytest .\session12.py
    # -v znamena verbozitu to znamena UKECANOST
    # python.exe -m pytest -v .\session12.py

    # TODO Napisat testy k lubovolnej funkcii

    # TDD - Test Driven Development


    print(ping_urllib('https://www.google.com')) # volame funkciu ping_urllib()

    '''
    PRIPOJENIE NA POCITAC POMOCOU MODULU SOCKET
    
    '''

    s = socket.socket()
    ADRESA = '192.168.254.1'
    PORT = 80  # SSH  #80 HTTP #21 FTP
    try:
        print("SKUSAME SA NAPOJIT NA ADRESU", ADRESA, PORT)
        t1 = time.time()
        s.connect((ADRESA, PORT))
        print((time.time()-t1)*1000.0)
        print("BINGO")
    except Exception as e:
        print(e.__repr__(), e)
    finally:
        pass

    print(portscanner("127.0.0.1"))  # 192.168.0.1. # volame funkciu portscanner()

    # TODO Prestavka 20:15
    '''
    KRYPTOGRAFIA SBOX ENCRYPTION pre Stream Dat
    '''
    
    # DES - TripleDES

    # AES - Rjijandel
    # Serpent



    # enc_znak = sbox_enc(sbox=sbox, key="B")
    # print(enc_znak)  # 173 ^ 55 = 154
    msg = "BRYNDZAZDRAZELA"
    #B (66)>85>109> 52> 223> 160> 250> 173 --> 154
    sbox = [23, 56, 89, 235, 127, 90, 87, 55]


    enc_msg = []
    for key in msg:  # Ideme cez BRYNDZA...
        enc_key = sbox_enc(sbox=sbox, key=key). # volame funkciu sbox_enc()
        print(enc_key)
        enc_msg.append(enc_key)

    print(enc_msg)

    # [154, 138, 129, 150, 156, 130, 153, 130, 156, 138, 153, 130, 157, 148, 153]  BRYNDZAZDRAZELA

    # TODO Domaca uloha spravit decrypt [154, 138, 129, 150, 156, 130, 153, 130, 156, 138, 153, 130, 157, 148, 153]
    '''
    A L G O R I T M U S  -  N A J K R A T S I A   C E S T A
    '''
    # musime si zadfinovat mnozinu bodov s prepojeniami
    graph = dict()
    graph["BA"] = ["TT"]
    graph["TT"] = ["BA", "NI", "PN"]
    graph["NI"] = ["TT", "BB"]
    graph["PN"] = ["TT", "TN"]
    graph["BB"] = ["KE", "NI"]
    graph["TN"] = ["ZA", "PN"]
    graph["KE"] = ["BB"]
    graph["ZA"] = ["PP", "TN"]


    print(najkratsia_cesta(graph, "TT", "KE")). # volame funkciu najkratsia_cesta()

    # TODO Spravit graph na hlavne mesta Europy.
