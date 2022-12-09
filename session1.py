'''
SESSION 1 - Z A K L A D N Y  K A M E N   P Y T H O N U



NAS PRVY PROGRAM AHOJ SVET

INTEGER - C E L E  C I S L O

FLOAT - C I S L O  S  D E S A T I N N O U   C I A R K O U

BOOL  - L O G I C K A   H O D N O T A

STRING - Textove retazce

FOR - jednoduchy cyklus na opakovanie prikazov

WHILE - cyklus

NAS DRUHY PROGRAM  - OZUBENE KOLIESKO /METAL GEAR/

LIST - ZOZNAM OBJEKTOV

IF logicky blok - jednoducha podmienka AK

'''
print("Hello World")

'''
INTEGER - C E L E  C I S L O
'''
if __name__ == '__main__':
    # cele_cislo = int()
    cele_cislo = 45  # vlozil som cele cislo do premennej cele_cislo
    cele_cislo = "AHA"  # prepisal som premennu a vlozil tam textovy retazec tzv. STRING
    vypocet = cele_cislo * 2  # vytvoril som novu premennu vypocet a vlozil tam premennu cele_cislo * 2

    print(cele_cislo, vypocet)  # vytlac do konzoly obsah suflikov cele ceislo a vypocet

    cele_cislo *= 2  # pythonisticka skratena forma  a = a * 2
    print(cele_cislo)  # TODO dorob nejaky iny vypocet

    '''
    FLOAT - C I S L O  S  D E S A T I N N O U   C I A R K O U
    '''


    cislo_s_desatinnou_ciarkou = float()  # vytvoril som prazdnu premennu, ktora bude obsahovat cislo s desatinnou ciarkou
    cislo_s_desatinnou_ciarkou = 2.65776  # vlozil som do nej cislo s desatinnou ciarkou

    print(cislo_s_desatinnou_ciarkou+0.3)  # vytlacil som premennu ale pridal som 0.3
    cislo_s_desatinnou_ciarkou += .3  # skratena forma suctu
    print(cislo_s_desatinnou_ciarkou)  # vytlacime premmenu do konzoly (textoveho vystupu Pythonu)
    vypocet = int(cislo_s_desatinnou_ciarkou)  # zmenim vypocet a vlozim don konverziu floatu na Integer (cele_ cislo)
    vypocet = float(vypocet)  # skonvertujem ho naspat
    '''
    POZOR konverzia nezaokruhluje ale odstranuje zbytky !!! 
    '''

    print(vypocet)

    '''
    BOOL  - L O G I C K A   H O D N O T A
    '''


    pravda = bool()  # vytvaram logicku premnenu Bool
    pravda = True  # Vkladam do nej hodnotu True PRAVDA
    print(pravda)  

    '''
    S T R I N G Y - Textove retazce
    '''

    # textovy_retazec = str()
    # text = ""
    textovy_retazec = "toto som teraz vymyslel."  
    print(textovy_retazec)
    print("teraz" in textovy_retazec)
    dlzku_textu = len(textovy_retazec)
    print(dlzku_textu)

    print(textovy_retazec.capitalize())
    print(textovy_retazec.upper())
    print(textovy_retazec.lower())
    print(textovy_retazec.isupper())

    print(textovy_retazec.count("to"))
    print(textovy_retazec.split(" "))
    # [slovo1,slovo2,slovo3]

    textovy_retazec = textovy_retazec + "\n\n" + textovy_retazec + "\t\t\t Ahoj"
    print(textovy_retazec)

    print(textovy_retazec[0])
    print(textovy_retazec[6:12])
    print(textovy_retazec[-1])

    textovy_retazec = "AHOJ"

    '''
    FOR - jednoduchy cyklus na opakovanie prikazov
    '''

    for i in range(0,10):
        print(i, textovy_retazec) # vykona 10 krat
    print("KONIEC")

    for i in textovy_retazec:
        print(i)

    for i in range(0, len(textovy_retazec)):
        print(textovy_retazec[i])

    '''
    while - cyklus while  
    '''

    while True:
        for i in range(0, 10, 2):
            print(i, textovy_retazec)
        break

    # cyklus ktory 32 zopakuje prikaz
    print("OK")

    '''
    NAS DRUHY PROGRAM  - OZUBENE KOLIESKO
    '''

    counter = 0  # definujem novu premennu suflik a vkladam do neho 0
    for i in range(0,32):
        print(i, counter, "UROB VOLACO")
        counter += 1  # zvys cislo v sufliku counter o 1

    # TODO PRESTAVKA DO 20:00 :)

    '''
    LIST - ZOZNAM OBJEKTOV
    '''

    zoznam_potravin = list()  # define new list
    zoznam_potravin = []
    zoznam_potravin = ["chlieb", "maslo", "mlieko"]
    print(zoznam_potravin)
    zoznam_potravin.append("kecup")  # pridaj do zoznamu kecup
    print(zoznam_potravin)
    zoznam_potravin.remove("kecup")  # odstran polozku kecup
    print(zoznam_potravin)

    print(zoznam_potravin[0])
    print(zoznam_potravin[-1])
    print(zoznam_potravin[1:3])
    print(len(zoznam_potravin))

    for i in zoznam_potravin:
        print(i)

    konstanty = tuple()
    konstanty = ("chlieb", "maslo")
    print(konstanty.count("maslo"))
    print(konstanty.index("chlieb"))

    zoznam = ["mlieko", "mlieko", "pomarance"]
    ovocie_set = set()

    zoznam_set = set(zoznam)

    # meno = input("ZADAJ MENO : ")

    '''
    IF logicky blok - jednoducha podmienka
    '''

    pocitadlo = 0
    while True:
        print("AHA")
        pocitadlo += 1
        # LOGIKA
        if pocitadlo > 50:  # podmienka , ktoru treba skontrolovat
            print("DOKONCIL SOM")
            break

     '''
     IF - ELSE  - podmienka s 
     '''

    a = False
    if a is True:
        print("PRAVDA")
    else:
        print("NEPRAVDA")

    if a is True and zoznam_set.count("maslo") == 1:  # and or not
        print()

     #   != NEROVNA SA
    a = 5435
    if a == 5435: print("VOLACO")
    if a <= 5435: print("")
    a = False
    if a == False:
        print("VOLACO")





