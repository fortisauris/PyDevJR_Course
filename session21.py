'''
SESSION 21 - OPENPYXL, PYTEST, NTPClient, QUASIDES
'''

# ROZCVICKA - Upratovanie :

# spravime si nejaky zoznam kde bude aspon 5

# zoznam = [1,2,3,4,5]  # stringy, cisla,

# pomocu cyklu budeme vytahovat clenov a vkladat ich do druheho zoznamu

# pomocou if nastavte, ze nejake hodnoty vyhodime pomocou prikazu del, remove

'''
OpENPYXL - Nacitanie suboru z Excelu do OPENPYXL a ulozenie zmien
'''

# pokracujeme OPXL_Load.py

'''
TESTOVANIE POMOCOU PYTESTU
'''

import pytest
from vstupy.skuska import nejaka_funkcia

def vyber_hodnotu(n: int):
    try:
        if n >= 0:
            return True
        else:
            return False
    except TypeError:
        print('NEVYHOVUJUCA HODNOTA')
        return False
    finally:
        pass


def vrat_hodnotu(inp):
    output = inp * 9
    return output

# ZAKLADNE TESTOVANIA s PYTEST
# python.exe -m pytest -v ./session21.py

@pytest.fixture()   # fixtures nam pomahaju oklamat test a dat mu vstupy ake potrebuje
def falosny_input():
    input_name = 'Frantisek'
    return input_name


@pytest.mark.ine
def test_value():
    assert vyber_hodnotu(5) is True
    assert vyber_hodnotu(-5) is False

@pytest.mark.string
def test_name(falosny_input):
    assert falosny_input == 'Frantisek'

@pytest.mark.ine
def test_vacsi():
    assert vyber_hodnotu(21) is not False

@pytest.mark.parametrize('inp', [-21,'str',None ])
def test_mensi(inp):
    assert vyber_hodnotu(inp) is not True

@pytest.mark.parametrize('inp, output', [(1, 9), (2, 18), (-9, -81)])
def test_mensi_2(inp, output):
    assert vrat_hodnotu(inp) == output


# python.exe -m pytest -k mensi -v ./session21.py   # SELEKTIVNE SPUSTANIE TESTOV PODLA KLUCOVEHO SLOVA

# python.exe -m pytest -m ine -v ./session21.py  # SELEKTIVNE SPUSTANIE TESTOV PODLA ZNANIEK @pytest.mark
# python.exe -m pytest -m ine -v ./session21.py

'''
VYTVARAME BALICKY
'''
# 1 - Kazdy script v zakladnom adresari projektu je automaticky pridany ako modul
# 2 - Balicek je adresar obsahujuci Pythonove subory(moduly), ktore mozno importovat
# 3 - Musi obsahovat subor __init__.py , ktory je v 99% pripadov prazdny

# 4 - Ak chceme spustat testy z podadresara testy musime adresar pridat do sys.path pomocou:

import os
import sys

PROJECT_PATH = os.getcwd()
sys.path.append(PROJECT_PATH)

# Import z balicka vstupy
sl = {'Hodnota1': 54354, 'Hodnota2': 643625, 'Hodnota3': True}
print(nejaka_funkcia(sl))

# TODO Prestavka do 20:10
'''
A L G O R I T M U S   D N A
'''

# Pokracujeme NTPclient.py v balicku vstupy


'''
K R Y P T O G R A F I A  - P R I M A R N A   P E R M U T A C I A   D E S U
'''
# pokracujeme QuasiDES.py