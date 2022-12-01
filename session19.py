
# KONVERZIA RIMSKYCH CISLIC NA ARABSKE CISLICE -  R O Z C V I C K A

# od I - M  dlzka retazca bude mas 4znaky I - VIII  #MCCM

def menic_znakov(znak: str):
    if znak == 'M':
        return 1000
    if znak == 'D':
        return 500
    if znak == 'C':
        return 100
    if znak == 'L':
        return 50
    if znak == 'X':
        return 10
    if znak == 'I':
        return 1
    return 1

# MCM  - 2000 + 100 = 2100 MMC
# return integer -cele cisla

# algoritmus konverzie ->   IX  mensie cislo je pred vacsim    XI vacsie cislo je pred mensim
rimske_cislo = 'XI'
# konverovat 1znak
if len(rimske_cislo) == 1:
    rimske_cislo = menic_znakov(rimske_cislo)
    print(rimske_cislo)

# konvertovat 2znak -- POZOR NA LOGIKU
if len(rimske_cislo) == 2:
    vysledok = 0
    pismeno1 = rimske_cislo[0]
    pismeno2 = rimske_cislo[1]
    pismeno1 = menic_znakov(pismeno1)
    pismeno2 = menic_znakov(pismeno2)
    if pismeno1 >= pismeno2:
        vysledok = pismeno1 + pismeno2
        print(vysledok)
    if pismeno1 < pismeno2:
        vysledok = pismeno2 - pismeno1
        print(vysledok)

# TODO Domaca uloha vytvorit algoritmus

    print(rimske_cislo)
# konvertovat 3 znaky

# VIII a XIII

'''
O P E N P Y X L   - B A S I C S 

'''

# Obalka s jupyter notebookom

# pokracujeme v OPXLS.py

#  K R Y P T O G R A F I A  -  Bitwise POSUN v bitoch

a = bin(65)
print(a)
a = 65 << 3
print(bin(a))
print(a)
a = a >> 9
print(a)

msg = 'BRYNDZAZDRAZELA'
enc = []
for pismeno in msg:
    posun = ord(pismeno) << 7
    print(ord(pismeno), posun, bin(posun))
    enc.append(posun)
print(enc)

decr = ''
for pismeno in enc:
    posun = pismeno >> 7
    print(pismeno, chr(posun), bin(posun))
    decr += chr(posun)

print(decr)


# TODO Domaca Uloha spravit posun podobne ako posun valcov pri Enigma
# string = '0000001'
# cyklus kolkokrat treba posunut
posun = string[1:] + string[0]

