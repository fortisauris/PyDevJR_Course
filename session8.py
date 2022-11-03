
# SKusanie slovicok z anglictiny - z cudzieho jazyka

# Slovnik kde budu slovicka  dict()  {"dog":"pes", "cat":"macka", "duck": "kacka"}
# nahodne vyberat slovicka  random.choice()  treba vyberat kluce keys() zo Slovnika
# zobrazime to slovicko na niekolko sekund  # time.sleep(5)
# napiseme jeho vyznam - zadame odpoved  # inputu("ZADAJ ODPOVED :")
# porovname ju  if odpoved == odpoved zo slovnika
# pridame za kazde uhadnute slovicko 5 bodov  # pridame skore do premennej skore

# funkcia na vymazavanie obrazovky - pre pokrocilych
# funkcia na pridanie do slovnika - pre pokrocilych
# ukoncenie nekonecneho cyklu pomocou q

'''
A D V A N C E D  L I S T
'''


a = list()  # [] ekvivalent
print(type(a))

a.append("Jergus")
print(a)

a.extend(["Maros", "Roman"])
print(a)

a.insert(2, "Yveta")
print(a)

a.remove("Maros")
print(a)

meno = a.pop(-1)
print(a, meno)

meno = a.pop()  # [] volitelny argument
print(a, meno)

a.clear()  # ekvivalent prikazu del a[:]
print(a)

fruits = ["Banany", "Jablka", "Ananas", "kiwi"]
print(fruits.index("Jablka", 0, len(fruits)))
# print(fruits.index("Srobovak", 0, len(fruits)))  # index ked nenajde vyhodi chybu

print(fruits.count("Banany"))  # count ukazuje pocet

fruits.sort()
fruits.sort(reverse=True)
print(fruits)

print(fruits.sort())   # POZOR METODA VRATI NONE
fruits.reverse()  # POZOR METODA VRATI NONE
print(fruits)

fruits2 = fruits.copy()  # plytka kopia  ekvivalent copy.copy()
print(id(fruits))
print(id(fruits2))
print(id(fruits[0]))
print(id(fruits2[0]))

fruits2.insert(0, "Srobovak")
print(id(fruits2[0]))

# STACK
stack = [1, 2, 3, 4, 5]
print(stack.pop())
print(stack.pop())
stack.append(6)
print(stack)
del stack[:]
print(stack)

from collections import deque, ChainMap

queue = deque(["Anton", "Jozef", "Matus"])
queue.append("Yveta")
print(queue)
queue.popleft()
print(queue)

alpha = [1,2,3,4,5,6]
beta = ["Alpha", "Beta", "Gama"]
a = ChainMap(alpha, beta)
print(a)
for i in a:
    print(i)

'''
M O D U L   C S V
'''

import json

a = ['Data', {"World": 543543, "Amerika": 5435, "Europa":[5435, 7657, 4234]}]

vystup = json.dumps(a)
print(vystup)

vystup = json.dumps(a, separators=(",", ":"))
print(vystup)

vystup = json.dumps(a, separators=(",", ":"), sort_keys=True)
print(vystup)

vystup = json.dumps(a, separators=(",", ":"), sort_keys=True, indent=4)
print(vystup)

vstup = json.loads(vystup)
print(vstup)

'''
def save_json_file(filename_w_path: str, data: dict):
    with open(filename_w_path, mode="w", encoding="utf8") as f:
        json.dump(data, f, indent=4, sort_keys=True )
'''
def load_json_file(filename_w_path: str):
    with open(filename_w_path, mode='r', encoding="utf8") as f:
        loaded_data = json.load(f)
        # print(loaded_data)
    return loaded_data


# save_json_file("test.json", data=a)
data = load_json_file('test.json')
for i in data:
    print(i)

"""
Je cislo prvocislo ?  - P R O G R A M  N A  U C E N I E

"""

def is_prime(n: int):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                print(n, "nie je prvocislo")
                return False
            else:
                return True
    else:
        return False

result = list()
for i in range(1000):
    if is_prime(i) is True:
        result.append(i)
print(result)

'''
S T A V I A M E   E N I G M U   - 1 R O T O R
'''


# Mechanicka cast pohyblive rotory 3 a jeden Reverzny A - X, A - G,
# Elektricku cast Plugboard - kazde pismeno abecedy mozeme nahradit inym

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sprava = "BRYNDZAZDRAZELA"

i = abeceda.index("R")
nastaveny_valec = abeceda[i:] + abeceda[:i]
print(nastaveny_valec)


def posun_valca(nvalec: str):  # ide o prvotne nastavenie valca
    valec = nvalec[1:] + nvalec[0]
    print(valec)
    return valec

zasifrovana_sprava = ''  # str()
for i in range(0, len(sprava)):
    zasifrovany_znak = nastaveny_valec[abeceda.index(sprava[i])]
    zasifrovana_sprava += zasifrovany_znak
    nastaveny_valec = posun_valca(nastaveny_valec)
print(sprava)
print(zasifrovana_sprava)

# TODO Prestavka do 20:10


'''
ZETELLKASTEN system  - U K L A D A N I E   I N D E X U   A  K A R T I C I E K  D O   M A R K D O W N U
'''
import random  # generovanie cisel - id cislo

baza_dat = dict()  # tu budu vsetky nase data  SLOVNIK

def generuj_id():
    """
    Funkcia nam generuje id cislo karticky. Pomocou odkazov na id cislo vieme prepajat karticky
    s dalsimi poznatkami. ID
    :return:
    """
    id = random.randint(0, 1000000)
    if skontroluj_id_duplicitu(id) is False:
        file = "index.md"
        with open(file=file, mode='a', encoding="ascii") as f:  # mode a znamena ze prida na koniec suboru udaj
            prepared_id = str(id) + "\n"  # pridava ENTER aby boli cisla pod sebou
            f.write(prepared_id)  # uklada id do zoznamu
    return id


def skontroluj_id_duplicitu(id: int):
    """
    Funkcia kontroluje ci existuje duplicita medzi id cislami v databaze v subore index.md

    :param id:  cislo od 0 do 1000000
    :return:  Boolean hodnota ak je duplicita True ak nie je False
    """
    file = "index.md"
    with open(file=file, mode='r', encoding="ascii") as f:
        while True:
            nacitane_id = f.readline()
            if nacitane_id == id:
                return True
            elif nacitane_id == "":
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
    Funkcia pomocou ktorej definujeme novu karticku, ktora sa potom uklada do bazy_dat ale aj
    suboru pod nazvom karticky vo formate Markdown.
    :return: None
    """
    print("ZADAJ NOVU KARTICKU DO SYSTEMU ZETTELKASTEN")
    nazov_karticky = input("NAZOV KARTICKY")
    skontroluj_nazov_karticky(nazov_karticky)
    id_cislo = generuj_id()
    print(id_cislo)
    linky = zadaj_linky()  # Tu volame funkciu na zadanie liniek na karticku
    tagy = zadaj_tagy()  # Tu volame funkciu na zadavanie tagov na karticku
    obsah_karticky = input("TEXT KARTICKY")
    baza_dat[nazov_karticky] = [id_cislo, linky, tagy, obsah_karticky] # Tu sa uklada nova karticka do Slovnika
    # TODO Uloz hned karticku vo formate .md MarkDown  .rst
    meno_suboru = nazov_karticky + ".md"
    with open(file=meno_suboru, mode="w", encoding="utf8") as f:
        text = "# {0} \nID: {1}\n Linky: {2} \n Tagy: {3} \n\n Obsah Karticky: \n{4}"
        pripraveny_text = text.format(nazov_karticky,
                                      baza_dat[nazov_karticky][0],
                                      baza_dat[nazov_karticky][1],
                                      baza_dat[nazov_karticky][2],
                                      baza_dat[nazov_karticky][3]
                                      )
        f.write(pripraveny_text)
    return None


def skontroluj_nazov_karticky(nazov):
    """
    Funkcia kontroluje ci je nazov karticky vyplneny. Ak by nebol mohlo by to robit problemy pri
    vyhladavani v nasom systeme karticiek
    :param nazov:
    :return:
    """
    if nazov == "":
        print("NEVYHOVUJUCI NAZOV KARTICKY")
        nova_karticka()
    # TODO Skontroluj ci neexistuje duplicitna karticka


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


