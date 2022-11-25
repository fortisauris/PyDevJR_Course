'''

R O Z C V I C K A

Spravte funkciu, GENERATOR, ktora na zavolanie vrati MESIAC v Stringu Januar, Februar, Marec
'''

# def mesiace_generator():

# premenna s mesiacmi

# prechadzat hodnotami a vratit hodnotu mimo funkcie

# na vracanie z funkcie treba pouzit NIE RETURN !!!  treba pouzit yield

# cyklus alebo zavolat funkciu a vytiahnut z generatora hodnotu -- STRING MESIACA.


def mes_gen():
    mesiace = ('jan','feb','mar', 'apr')
    for i in mesiace:
        yield i

a = mes_gen()

print(next(a))
print(next(a))
print(next(a))


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

#  Pokracujeme v subore DA-CryptoC.ipynb

'''

P I L L O W   - Kniznica na pracu a upravu obrazkov

'''


# Pokracujeme v subore PIL-ManipulaciaJPEG.ipynb


'''
T R A N S P O Z I C N A   S I F R A

1   2   3 
4   5   6
7   8   9

3   4   5       
2   9   6
1   8   7


'''

def rozdel_dlzku(sekvencia, dlzka):
    return [sekvencia[i:i + dlzka] for i in range(0, len(sekvencia), dlzka)]  # Comprehension LIST, DICT


def zakoduj(kluc, msg):
    poradie = {
        int(val): num for num, val in enumerate(kluc)
    }
    # print(poradie)

    enc_text = ''
    for index in sorted(poradie.keys()):
        for cast in rozdel_dlzku(msg, len(kluc)):
            try:
                enc_text += cast[poradie[index]]

            except IndexError:
                continue
    return enc_text

msg = 'AHOJTESTRETNEMESAVPONDELOKNAKURZEOSEDEMNASTEJ'
enc_msg = ''
for i in range(0,len(msg), 9):
    # print(msg[i:i+9])
    enc_particle = zakoduj('630125874', msg[i:i+9])
    enc_msg += enc_particle
print(enc_msg, '\t', msg)
# print(zakoduj('53214', 'HELLO'))

# TODO Skusit Dekodovat spravu --- ODSLIMACIT
