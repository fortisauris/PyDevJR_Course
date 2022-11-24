# ROZCVICKA - ODPOCET DATUMU A CASU DO NAJBLIZSIEHO SPLNU MESIACA

# import datetime

# datetime.datetime.now()

# datetime object 8.12.2022 4:09

# datetime.timedelta()  # vypocitat a zobrazovat na obrazovke.

# ADVANCED : Dalsi spln mesiaca + 29.5 dni od SPLNU.

'''

 D A T A   S C I E N C E   -  L E K C I A  3  - P R A C A  S   D A T A S E T M I

'''

# Spustime si Virtualnu obalku v projekte CestaNaJupyter:

''''    /venv/Scripts/Activate.ps1      '''

# Ak Win vyhodi chybu v terminali tak

'''     Set-ExecutionPolicy Unrestricted -Scope Process     '''

# Ak mame nainstalovany Jupyter a Numpy(SESSION14) tak Nainstalujeme pandas a matplotlib pomocou pip

'''     skopirujeme si meteo.csv a obce_hustota.csv z adresara /PyDevJr/datasets/ do /CestaNaJupyter  '''

# Spustime jupyter

'''     jupyter notebook    '''

#  Pokracujeme v subore DA-Meteo.ipynb

# Pokracujeme v subore DA-Obce_Hustota.ipynb



'''
while True:
    try:
        print('VOLACO')
    except KeyboardInterrupt:  # zachytava Ctrl-C
        cmd = input("ZADAJ PRIKAZ :")
        if cmd == 'q':
            quit()
    finally:
        pass
'''

'''
T R A N S P O Z I C N A   S I F R A
'''

# SUBSTITUCNE SIFRY    A --> F
# TRANSPOZICNE SIFRY   HELLO - LOEHL  - IBA MENI PORADIE PISMEN POMOCOU SABLONY


def rozdel_dlzku(sekvencia, dlzka):
    return [sekvencia[i:i + dlzka] for i in range(0, len(sekvencia), dlzka)]  # Comprehension LIST, DICT


def zakoduj(kluc, msg):
    poradie = {
        int(val): num for num, val in enumerate(kluc)
    }
    print(poradie)

    enc_text = ''
    for index in sorted(poradie.keys()):
        for cast in rozdel_dlzku(msg, len(kluc)):
            try:
                enc_text += cast[poradie[index]]

            except IndexError:
                continue
    return enc_text

print(zakoduj('53214', '85467'))


