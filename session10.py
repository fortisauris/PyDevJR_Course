import os

# MAZACKU SUborov  - Rozcvicka

# funkcia mazanie_suborov( nazov suboru aj s cestickou )

# otvorime subor

# Potrebujeme dlzku suboru  file.read()  # len(string)

# TOTO NEPOUZIJEME os.system('rm file')

# prepiseme to 5 x pomocou cyklu

# pripravime si string  podla dlzky suboru str("1")

# print je to prepisane.

nas_set = {"alpha","beta", "delta", "gama", "gama"}  # set()
vzorka = set(["omega", "gama"])

print(nas_set)
print(len(nas_set))

print('beta' in nas_set)  # ci sa nachadza
print('gama' not in nas_set)  # ci sa nenachadza v sete
# skumaju ci su podmnozinou ineho setu
print(nas_set.isdisjoint(vzorka))
print(nas_set.issubset(vzorka))
print(nas_set.issuperset(vzorka))
# metody na ziskanie rozdielnych clenov
print(nas_set.union(vzorka))
print(nas_set.intersection(vzorka))
print(nas_set.difference(vzorka))
print(nas_set.symmetric_difference(vzorka))

novy_set = nas_set.symmetric_difference(vzorka).copy()  # plytku kopia  shallow copy
print(sorted(novy_set))
# Update setu  # modifikacia objektu

nas_set.update(vzorka)
print(nas_set)
nas_set.intersection_update(vzorka)
print(nas_set)
nas_set.difference_update(vzorka)
print(nas_set)
nas_set.symmetric_difference_update(vzorka)
print(nas_set)

nas_set.add("Ypsilon")
print(nas_set)
# nas_set.remove("theta")  # Pozor vyhadzuje Key Error
nas_set.discard("Ypsilon")
print(nas_set)

nas_set.clear()
print(nas_set)

print(novy_set)

nas_zamrznuty_set = frozenset(novy_set)
print(nas_zamrznuty_set)

# nas_zamrznuty_set.add("gama")
# a = nas_zamrznuty_set.pop()
# nas_zamrznuty_set.clear()

print(nas_zamrznuty_set)
for i in nas_zamrznuty_set:
    print(i)

'''
Globalne premenne

'''
#global val
# val = 65465

def vytlac_hodnotu():
    global val   # globalna premenna
    val = 534543
    return val

print(vytlac_hodnotu())
print(val)

class Baterka(object):
    # _znacka = "Duracell"  # PROTECTED
    __znacka = "Duracell"  # PRIVATE

    def __init__(self):
        self.model = "Extra Max"
        self.capacity = 2700 # mAh
        self.type = "NiMh"

    @property
    def vytlac_kapacitu(self):
        kapacita = self.capacity + 10
        print(self.__znacka)
        return kapacita


obj = Baterka()
#  print(obj.__znacka)  # Private
print(obj.model)
print(obj.capacity)
print(obj.type)
print(obj.vytlac_kapacitu)

# TODO Vyrobit Frozenset a vyuzit v jednoduchom programe - cyklus
# TODO Vyskusat triedu s Property a Privatnymi premennymi
'''
Jednoduchy Socket Server s Web Serverom v Pythone
'''
import http.server
import socketserver   # adresy IP 8.8.8.8  alebo URL - a PORTU 8000
# Lokalna IP: 127.0.0.1
# bezny pocitac ma 65535 PORTOV.
# webserver Apache, Nginx

PORT = 8000 # 80
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT), Handler) as httpd:  # UDP Neautorizovane ...
    print("serving at port :", PORT)
    httpd.serve_forever()
    
'''
Jednoduchy socket server s webserverom s upravenym handlerom aby poskytoval index.html
pomocou GET metody
'''


PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("HTTP Server poskytuje na porte :", PORT)
    httpd.serve_forever()

'''
Jednoduchy webserver, ktory poskytuje pomocou metody GET nami zadany kod. 
Pouzivame tu datetime.datetime.now() a zobrazujeme me ho na webe.
'''

from http.server import *
import datetime

class NAS_SERVER(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)  # Success

        self.send_header('content-type', 'text/html')
        self.end_headers()

        datum = "<h1>" + str(datetime.datetime.now()) + "</h1>"

        self.wfile.write('<h1> TOTO JE NAS PERFEKTNY SERVER </h1>'.encode())
        self.wfile.write('<p> Toto je nas text pre nasu webovu stranku </p>'.encode())
        self.wfile.write(datum.encode())

port = HTTPServer(('', 8000), NAS_SERVER)
port.serve_forever()

'''
B U B B L E   S O R T  A L G O R I T M U S
'''
def bubble_sort(array: list):
    dlzka = len(array)
    for i in range(dlzka):
        already_sorted = True  # Flagy

        for j in range(dlzka - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]  # prehadzovanie hodnot v zozname
                already_sorted = False  # Vlajocky
        if already_sorted:
            break
    return array   # vracia zoradeny zoznam


array = [5435,765,868,42,8768,9098,432,9687]
print(bubble_sort(array=array))


# TODO Prestavka do 20:10

'''
E N I G M A  - pridame si treti rotor
'''

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sprava = "BRYNDZAZDRAZELABRYNDZAZDRAZELA"

# R O T O R  1
i = abeceda.index("R")  # pociatocne nastavenie valca
nastaveny_valec_1 = abeceda[i:] + abeceda[:i]
print(nastaveny_valec_1)

# R O T O R  2
i = abeceda.index("S")  # pociatocne nastavenie valca
nastaveny_valec_2 = abeceda[i:] + abeceda[:i]
print(nastaveny_valec_2)

# R O T O R  3
i = abeceda.index("F")  # pociatocne nastavenie valca
nastaveny_valec_3 = abeceda[i:] + abeceda[:i]
print(nastaveny_valec_3)


def posun_valca(nastaveny_valec: str) -> str:
    '''
    Funkcia posun valca nam na zavolanie a zadanie rotora posunie rotor o jedno miesto
    :param nastaveny_valec: retazec znakov nastavenia rotora
    :return: rotor posunuty o 1
    '''
    valec = nastaveny_valec[1:] + nastaveny_valec[0]
    print(valec)
    return valec

'''
H L A V N Y  P R O G R A M  E N I G M Y
'''

zasifrovana_sprava = ""
posun_valcov = 0
for i in range(0, len(sprava)):
    enc_znak = nastaveny_valec_1[abeceda.index(sprava[i])]  #
    enc_znak = nastaveny_valec_2[abeceda.index(enc_znak)]
    enc_znak = nastaveny_valec_3[abeceda.index(enc_znak)]
    # TODO pridaj Reverzny valec
    # TODO pridaj Plugboard
    nastaveny_valec_1 = posun_valca(nastaveny_valec_1)

    if posun_valcov == 26:
        nastaveny_valec_2 = posun_valca(nastaveny_valec_2)  # TODO Ak Valec 2 dosiahne 26 ???
        posun_valcov = 0
    zasifrovana_sprava += enc_znak
    posun_valcov += 1

print(sprava)
print(zasifrovana_sprava)
