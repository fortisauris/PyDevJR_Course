'''
ZETELLKASTEN system
'''
import random  # generovanie cisel - id cislo
import os  # manipulacia s adresarmi a subormi

baza_dat = dict()  # tu budu vsetky nase data  SLOVNIK


def zberatel_karticiek():
    """
    Tato funkcia bude zbierat karticky a porovnavat ich s ID cislami v Indexe.
    Potom obsah karticiek nasype do BAZY_DAT.
    :return: zoznam suborov v adresari.
    """
    index = list()
    with open("index.md", mode='r', encoding='utf8') as f:
        raw_index = f.read()
        for i in raw_index.split('\n'):
            if i.isnumeric():
                index.append(i)
            else:
                print("NIE JE CISLO")
    print(index)
    # TODO v buducnosti prezerat podadresare pomocou os.walk()
    zoznam_md_suborov = list()
    print(os.getcwd())
    for i in os.listdir(path=os.getcwd()):  # Current Working Directory
        if i.endswith(".md"):
            zoznam_md_suborov.append(i)
    zoznam_md_suborov.remove("index.md")  # Automaticky nam vyhodi index.md zo zoznamu karticiek
    print(zoznam_md_suborov)
    return zoznam_md_suborov

def nahraj_karticky(zoznam: list):
    """
    Funkcia ktora nacitava vsetky karticky zo zoznamu karticiek, ktory vytvoril Kolektor_karticiek().
    Nacitava ich do pamate a uklada do slovnika baza_dat. Takto potom dokazeme v programe zobrazit
    uz existujuce karticky a nemusime ich pomocou programu zadavat nanovo.
    :param zoznam: zoznam existujucich suborov .md okrem index.md List
    :return: None - udaje idu automaticky do slovnika baza_dat
    """
    for i in zoznam:
        with open(file=i, mode='r', encoding='utf8') as f:
            obsah = f.read()
            print(obsah)
            raw_karticka = obsah.split("\n")
            # Odstrani prazdne riadky
            for k in range(raw_karticka.count("")):
                raw_karticka.remove('')
            # Ide vkladat do Bazy dat
            baza_dat[raw_karticka[0][2:]] = list()
            baza_dat[raw_karticka[0][2:]].append(raw_karticka[1])
            baza_dat[raw_karticka[0][2:]].append(raw_karticka[2])
            baza_dat[raw_karticka[0][2:]].append(raw_karticka[3])
            baza_dat[raw_karticka[0][2:]].append(raw_karticka[4])
            # print(baza_dat[raw_karticka[0][2:]])
            # print(raw_karticka)
    return


def generuj_id():
    """
    Funkcia nam generuje id cislo karticky. Pomocou odkazov na id cislo vieme prepajat karticky
    s dalsimi poznatkami
    :return:
    """
    id = random.randint(0, 1000000)
    if skontroluj_id_duplicitu(id) is False:
        file = "index.md"
        with open(file=file, mode='a', encoding="ascii") as f:  # mode a znamena ze prida na koniec suboru udaj
            prepared_id = str(id)+"\n"  # string ktory sa zapise
            f.write(prepared_id)
    return id


def skontroluj_id_duplicitu(id: int):
    """
    Funkcia kontroluje ci existuje duplicita medzi id cislami v databaze
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
    print("NAZOV KARTICKY", "ID KARTICKY", "LINKY", "TAGY", "TEXT KARTICKY")
    for i in baza_dat.keys():
        print(i, baza_dat[i][0], baza_dat[i][1],  baza_dat[i][2], baza_dat[i][3] )
    return

def skontroluj_ci_existuje(file: str):
    """
    Funkcia kontroluje ci subor existuje na disku pomocou os.listdir().
    Povodne bola urcena iba na detekciu suboru index.md, ktory ked nenajde tak ho vytvori.
    Bola doplnena o kod, ktory nam vracia Boolean ci subor existuje alebo nie
    :param file: meno suboru s cestickou  String
    :return: Boolean
    """
    adresar = os.getcwd()  # ziskame info o pracovnom adresari
    zoznam_suborov = os.listdir(adresar)  # pomocou os.listdir si vypiseme vsetky subory v adresari
    # print(zoznam_suborov)
    if file not in zoznam_suborov and file == "index.md":  # ak index.md nie je v zozname --> UROB
        with open(file="index.md", mode="w", encoding="utf8") as f:  # Vytvori prazdny index.md
            f.write("# Index of IDs\n")
            print("SUBOR index.md BOL VYTVORENY !!!")
            return False
    elif file in zoznam_suborov:
        print("SUBOR NAJDENY")
        return True
    elif file not in zoznam_suborov:
        print("SUBOR NENAJDENY")
        return False
    else:
        print("SUBOR index.md BOL NAJDENY !!! ")  # Vsetko v poriadku, subor sa nasiel
        return True

def nova_karticka():
    """
    Funkcia pomocou ktorej definujeme novu karticku a vkladame jej udaje do bazy_dat slovnika
    a zaroven ukladame subor vo formate .md a prednastavenej sablone
    #TODO Pridat moznost prepisovat sablony
    :return:
    """
    print("ZADAJ NOVU KARTICKU DO SYSTEMU ZETTELKASTEN")
    nazov_karticky = input("NAZOV KARTICKY")
    skontroluj_nazov_karticky(nazov_karticky)
    id_cislo = generuj_id()  # funkcia ktora generuje id
    print(id_cislo)
    linky = zadaj_linky()  # Tu volame funkciu na zadanie liniek na karticku
    tagy = zadaj_tagy()  # Tu volame funkciu na zadavanie tagov na karticku
    obsah_karticky = input("TEXT KARTICKY")
    baza_dat[nazov_karticky] = [id_cislo, linky, tagy, obsah_karticky] # Tu sa uklada nova karticka do Slovnika

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
        print("SUBOR KARTICKY BOL ULOZENY")
    return None


def skontroluj_nazov_karticky(nazov):
    """
    Funkcia kontroluje ci nazov karticky zodpoveda poziadavkam. Nesmie byt prazdny ""
    a zaroven kontroluje duplicita ci uz taka karticka nebola ulozena na disku.
    :param nazov:
    :return:
    """
    if nazov == "":  # NESMIE BYT PRAZDNY
        print("NEVYHOVUJUCI NAZOV KARTICKY")
        nova_karticka()
    meno_suboru_karticky = nazov+".md"
    if skontroluj_ci_existuje(meno_suboru_karticky) is True:
        print("KARTICKA UZ EXISTUJE !!!")
        nova_karticka()


def zadaj_linky():  # [[id]]
    '''
        Funkcia na zadavanie linkov, ktore radia karticky do mnozin podla problematiky.
        Je potrebne aby funkcia umoznovala vkladat viacero linkov a upravovat ich format
        pridanim [[ na zaciatok retazca a ]] na koniec retazca. Zadanim q opustime funkciu a vratime sa
        do zadavana alebo editovania karticky.
        :return: None
    '''
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
    '''
    Funkcia na zadavanie tagov, ktore radia karticky do mnozin podla problematiky.
    Je potrebne aby funkcia umoznovala vkladat viacero tagov a upravovat ich format
    pridanim hashtagu na zaciatok retazca. Zadanim q opustime funkciu a vratime sa
    do zadavana alebo editovania karticky.
    :return: None
    '''
    # TDO SPrav spolocnu funkciu pre zadavanie Tagov aj Linkov
    result = list()
    while True:
        command = input("ZADAJ TAG ALEBO q PRE UKONCENIE")
        # TODO Pridaj kod, ktory bude kontrolovat ci tag zacina # aby tam neboli dva ##
        if command == "q":
            break
        else:
            prepare_link = "#" + command + " "
            print(prepare_link)
            result.append(prepare_link)
        # TODO Sprav funkciu, ktora bude vyberat z existujucich tagov
    print(result)
    return result


while True:
    ''' Nastavenia a kontroly programu'''
    
    skontroluj_ci_existuje("index.md")
    
    # TU DOJDE KOLEKTOR KARTICIEK
    index = zberatel_karticiek()
    print(index)
    nahraj_karticky(index)

    
    """ HLAVNY PROGRAM, KTORY POMOCOU NEKONECNEHO CYKLU PRIJIMA PRIKAZY OD UZIVATELA"""
    cmd = input("ZADAJ PRIKAZ q-quit|n-new|v-view")  # vstup z klavesnice uzivatela
    if cmd == "q":  # ak je command q -> ukonci program
        break
    elif cmd == "n":  # ak je command n -> vytvor novu karticku
        nova_karticka()  # vola funkciu nova karticka
    elif cmd == "v":  # ak je prikaz v -> zobraz zakladny vypis z dayabazy
        basic_view()  # vola funkciu zakladny vypis
