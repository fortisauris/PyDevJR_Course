"""
M O D U L  D A T E T I M E
"""

import datetime
import zoneinfo
import tzdata

d1 = datetime.date(year=2022, month=11, day=3)
print(d1)
print(type(d1))
print(d1.timetuple())  # time.localtime()
print(d1.toordinal())
print(d1.weekday())  #
print(d1.isoweekday())  #
print(d1.isocalendar())
print(d1.isoformat())
print(d1.ctime())

d2 = datetime.date(1989,11,17)
print(d2.toordinal())
print(d2.ctime())
print(d2.strftime("%A %d.%B %Y %z"))

d_final = d1-d2  # datetime.date - datetime.date = datetime.timedelta
print(type(d_final))
print(d_final)

t1 = datetime.time(11,2,30,0)
print(type(t1))
print(t1)

zone = zoneinfo.ZoneInfo("Europe/Bratislava")
dt = datetime.datetime(year=2022, month=11, day=3, hour=17, minute=50, second=30, microsecond=0, tzinfo=zone)
print(dt.tzinfo)

dt2 = datetime.datetime(year=2021, month=10, day=1, hour=12, minute=30, second=0, microsecond=0, tzinfo=zone)
print(dt.tzinfo)

d_final = dt - dt2

print(type(d_final))
print(d_final)
print(d_final.total_seconds())
'''

for i in zoneinfo.available_timezones():
    if i[:2] == "Eu":
        print(i)
'''

dn = datetime.datetime.now()
print(dn)

cet = datetime.timedelta(hours=1)  # posunuta o 1 hodinu od GMT
tz = datetime.timezone(offset=cet)

dt3 = datetime.datetime(year=2022, month=3, day=8, hour=11, minute=34, tzinfo=tz)
print(dt3)

zajtra = datetime.datetime.now() + datetime.timedelta(days=1)
print(zajtra)

print(zoneinfo.ZoneInfo("Europe/Madrid"))

# vytvorte jeden datumovy datetime.datetime() objekt
# vytvortte druhy datumovy datetime.datetime() objekt
# tieto dva objekty zratajte alebo odratajte


# zobrazte casovy rozdiel medzi tymico objektami
# pridat nejaky standarny cas na odbavenie na letisku ... 1h
# zobrazit cas

'''
A D V A N C E D   D I C T
'''

a = dict() # ekvivalent je {}
a = dict(one=1, two=2, three=3)
print(a)
b = {"one":1,
     "two":2,
     "three":3
     }
print(b)

c = dict(zip(["one", "two", "three"], [1,2,3]))
print(c)
print(list(c))
print(len(c))

print(c["one"])
# print(c["haluska"])  # vyhodi KeyError

c['four'] = 4
print(c)

del c["four"]
print(c)

print("one" in c)
print("three" not in c)

a = iter(c)
for i in range(0, len(c)):
    print(i, next(a))

c.clear()
print(c)

c = b.copy()  # plytka kopia objektu
vystup = c.fromkeys(c.keys())
print(vystup)

print(c.get("one"))

print(c.keys())
print(c.values())
print(c.items())

c.pop("one")
print(c)

val = c.popitem()
print(val, "\n", c)


c = b
print(c)
c_it = reversed(c)
print(c_it.__next__())
print(c_it.__next__())
print(c_it.__next__())

c.setdefault('four', True)
c.setdefault("one", True)
print(c)

c.update(b)
print(c)

# dictview objects
print(len(c.items()))
a = iter(c.keys())
for i in range(0, len(c.keys())):
    print(a.__next__())

print('one' in c.keys())
print(True in c.values())

a = reversed(c.items())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

'''
Premena decimalneho cisla na binarne
'''

def dec2bin(n: int):
    vysledok = ""
    if n == 0:
        return 0
    while n:
        vysledok += str(n&1)
        n = n >> 1

    vysledok = vysledok[::-1]

    return vysledok

print(dec2bin(6))
print(bin(6))
print(hex(60))
print(oct(60))
print(chr(65))  # kod ASCII pre A
print(ord("A"))  # ukazuje kod ASCII tabulky


'''
E N I G M A  - pridame si dalsi rotor
'''

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sprava = "BRYNDZAZDRAZELABRYNDZAZDRAZELA"

i = abeceda.index("R")  # pociatocne nastavenie valca
nastaveny_valec_1 = abeceda[i:] + abeceda[:i]
print(nastaveny_valec_1)

i = abeceda.index("S")  # pociatocne nastavenie valca
nastaveny_valec_2 = abeceda[i:] + abeceda[:i]
print(nastaveny_valec_2)


def posun_valca(nastaveny_valec):
    valec = nastaveny_valec[1:] + nastaveny_valec[0]
    print(valec)
    return valec


zasifrovana_sprava = ""
posun_valcov = 0
for i in range(0, len(sprava)):
    if posun_valcov <= 26:
        enc_znak = nastaveny_valec_1[abeceda.index(sprava[i])]  #
        nastaveny_valec_1 = posun_valca(nastaveny_valec_1)
        # TODO Zamysliet sa ako to spravit aby hodnota bola posuvana na oboch valcoch
    if posun_valcov > 26 and posun_valcov < 52:
        enc_znak = nastaveny_valec_2[abeceda.index(sprava[i])]
        nastaveny_valec_2 = posun_valca(nastaveny_valec_2)
    zasifrovana_sprava += enc_znak
    posun_valcov += 1

print(sprava)
print(zasifrovana_sprava)

# TODO Pauza do 20:15







