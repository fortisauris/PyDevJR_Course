# ROZCVICKA  - softver katalog knih

# funkciu na pridavanie kniziek do zozonamu
#    kniznica.append(kniha)

# funkciu na vymazavanie kniziek zo zoznamu
#    kniznica.remove(kniha)  # POZOR NA ERROR

# funkciu na prezerenia kniziek pod sebou
#    cyklus for v kniznici a vypisat pod seba knihy

# kniznica = list()  # pokrocily dict(), ISBN, datum

'''

O P A K O V A N I E   Z A K L A D N E H O   S Y N T A X U

'''


# VARIABLES

# INTEGER
a = int()
a = 4637673
print(type(a))
print(dir(a))

# STRINGY
text = str()
text = 'text'
text = 2 * text
text[0]
text[-1]
print(type(text))
print(dir(text))

a = float()
a = 43.5647654

flag = True
flag = False

a = bytes('hfjdshfjd', encoding="utf8")
print(a)

print("AHA")
# input()
# quit()

list()   # mutovatelnost, flexibility
tuple()
set()  # sa neopakuje clenovia
frozenset()  # zamrznuty
dict()

# cykly

for i in range(5):
    print(i)

b = 0
c = 0
while c < 10:
    print("UROB VOLACO")
    c += 1

# riadenie toku programu
if c == 10:
    print('c=10')
elif c > 10 and b != 0:
    print('c je viac ako 10')
else:
    print('c je mensie ako 10')


# continue
# break

def sucet_fn(a, b):
    return a + b

sucet = lambda a,b: a + b

print(sucet_fn(2,2))
print(sucet(2, 2))


# Triedy
class Ponozka(object):

    def __init__(self):  # Constructor
        self.status = 'cista'
        self.material = 'bavlna'
        print("VZNIKLA NOVA PONOZKA")

    def __del__(self):  # DESTRUCTOR
        print("ZANIKLA PONOZKA")
        return

    def __repr__(self):
        return "OBJEKT TRIEDY PONOZKA"

    def status_setter(self, status):
        self.status = status


obj = Ponozka()
obj.status_setter('spinava')
print(obj.status)
print(obj.__repr__())
del obj

# ZACHYTAVANIE CHYB
try:
    a = 54543/0
except ZeroDivisionError:
    print("NEMOZES DELIT NULOU !!!")
    a = 54543/1
finally:
    print(a)

'''
D E P E N D E N C I E S  - Softver, ktory musi byt nainstalovany
'''

# Zettelkasten  Python 3.9 a dalsie verzie   DEPENDENCIES
# Dalsie Dependacies  - pyqt, tkinter, SQLAlchemy, redis
# IDEME VYTVORIT VIRTUALNU OBALKU S CISTYM PYTHONOM

''' python.exe -m venv <ADRESAR>  '''

# SPUSTIT VIRTUALNU OBALKU
# WIN
'''
Set-ExecutionPolicy Unrestricted -Scope Process
<Adresar>/Scripts/Activate.ps1
'''
#LINUX/MAC
'''
source <ADRESAR>/bin/activate
'''
# Ak sa vsetko podari tak pred Promptom bude nazov Vasej obalky

# INSTALUJEME SOFTVER
'''     pip3 install jupyter    ALEBO   python.exe -m pip install jupyter   '''

# VYPNUTIE UKONCENIE OBALKY
''' deactivate  '''

''' J U P Y T E R   N O T E B O O K'''
# Nastroj na vytvaranie interaktivnych dokumentov so spustitelnym python kodom
# a textovymi, grafickymi ci inymi castami

# SPUSTIME
''' jupyter notebook    '''
# Spusti sa server a poskytne linku, na localhoste, ktoru treba otvorit v Browseri
# Dame New Notebook
'''
SPUSTANIE KODU V RIADKU   Alt-Enter

'''
# Notebooky mozno zdielat, publikovat, prezentovat a su vhodne najma na vedecku pracu s datami, algoritmami
# vyucbu, datovu analytiku atd.





# TODO Prestavka do 20:11

# www.realpython.com

# TODO Spravit Basic git manual
'''
G I T   - V E R S I O N   C O N T R O L
'''
# uklada a sleduje zmeny v kode a umoznuje sa vracat v case ked sa nieco pokazi
# pomaha pri vyvoji a umoznuje ukladat program na Cloude - Github
# Pomaha vyvijat softver v spolupraci s inymi programatormi
# a mnoho dalsieho


# NAKLONOVANIE REPOZITARA
''' git clone https://github.com/fortisauris/PyDevJR_Course.git  '''
# ZISTENIE STAVU
''' git status  '''
# STIAHNUTIE AKTUALNEHO STAVU S GITHUBU
''' git pull    '''





'''
A L G O R I T M U S  - P R I K L A D   R O Z D I E L Y   V  K O D E
'''

uzivatelia = [
    {"user": "jankoNeznamy", "vyska": 1.75},
    {"user": "mariaNeznama", "vyska": 1.68},
    {"user": "JankoEstemenejznamy", "vyska": 1.96},
]

# ZLY SPOSOB - PROCEDURALNY
najvyssi_user = ''
maximalna_vyska = 0

for user in uzivatelia:
    if user["vyska"] > maximalna_vyska:
        max_height = user["vyska"]
        highest_user = user

print(najvyssi_user, maximalna_vyska)

# DOBRY SPOSOB FUNKCIONALNY
najvyssi_user = max(uzivatelia, key=lambda user: user["height"])
print(najvyssi_user)


'''
S B O X   E N C R Y P T   - 2  S B O X Y
'''

sbox = [23, 56, 89, 235, 127, 90, 87, 55, 43]
sbox2 = [11, 76, 98,12,65,90,156,200]


def sbox_enc(sbox: list, key: int) -> int:
    '''
    Jednoducha funkcia na zasifrovanie znaku pomocou sboxu. Hodnota je postupne XOR nuta so vsetkymi clenmi
    sboxu.
    :param sbox: krabica s ciselnymi hodnotami od 0 do 255 :list
    :param key: ciselna hodnota znaku z ASCII tabulky znakov  : int
    :return: zasifrovany znak  :int
    '''
    for i in sbox:
        key ^= i  # XOR Operacia
        # print(i, key)
    return key  # zasifrovane pismeno

val = sbox_enc(sbox, ord("B"))
print(val)
sbox.reverse()
print(sbox)
val = sbox_enc(sbox, 154)
print(chr(val))
sbox.reverse()
print(sbox)

msg = "BRYNDZAZDRAZELA"
enc_msg = []
for i in msg:
    enc_znak = sbox_enc(sbox=sbox, key=ord(i))
    enc_znak = sbox_enc(sbox=sbox2, key=enc_znak)
    enc_msg.append(enc_znak)

print(enc_msg)

# TODO ZAjtra Decryption z dvoch sboxov spravit


