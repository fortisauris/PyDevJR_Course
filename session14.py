#

# spravte zoznam s minimalne troma hodnotami

# zoradte podla abecedy


'''

U V O D   D O   D A T A   S C I E N C E

opendata.bratislava.sk
opendata.kosice.sk
# TODO Najdite dalsie opendata stranky
'''
# TODO Spustit obalku v projekte CestaNaJupyter
# Nainstalovali sme numpy, pandas, matplotlib,

# Prvy Notebook opakovanie funkcionalneho programovania v Pythone

# Druhy Notebook - praca s arrays v numpy

'''

H M A C   M O D U L
'''

# GSM  900MHz digitalny A4 FQ Hopping

# NMT  - 400+ Mhz analog

'''
 vysledkom kryptografickeho algoritmu, ktory vypocit nieco ako otlacok a my vieme ze s datami nebolo manipulovane
'''

# MITM - Man In The Middle

# User -> Utocnik -> Server
# Hello -> SPravu, vypocita novy hash  -> Server  NEDOZVIE!!!

''' AUTENTIFIKACIA HASHSTRINGU  '''

import hmac

key = bytes('pomaranc', encoding='utf8')   # KNOWN SECRET, heslo, datum registracie, token
msg = bytes('7920b185315924d082f41e94ac8bf5b9' + str({"ucet1": 5438574, 'ucet2':463764836, 'amount':0.00002}), encoding='utf8')
h = hmac.new(key=key, msg=msg, digestmod='md5')
print(h.digest())   # bytes
print(h.hexdigest())  # hex

# TODO Prestavka - 20:10

'''
 B L O C K C H A I N   K O N C E P T
 
 V banke mas ucet  Andrej - 15EUR - 7EUR
 existuje nejaka databaza a v    

'''

andrejov_ucet = {'cislo uctu': 463764836, 'amount': 15}    # 7EUR mesacne 84EUR rocne.

databaza = []

# RETAZ DAT

# PRVY KROK
{'cislo uctu': 463764836, 'amount': 150}  # vypocitame e559502cf540ab4b00dd02ea4a323454  -->

# DRUHY KROK
'e559502cf540ab4b00dd02ea4a323454' + str({'cislo uctu': 5438574, 'amount': 15})  # vypocitame 7920b185315924d082f41e94ac8bf5b9 -->

# TRETI KROK
'7920b185315924d082f41e94ac8bf5b9' + str({"ucet1": 5438574, 'ucet2':463764836, 'amount':0.00002})  # 2df12f318cf11042220bc5c8fbfcaad1

# STVRTY BLOK
'2df12f318cf11042220bc5c8fbfcaad1' +

# KAKAO 0.00002 BTC

# 70 %

# vypocitaju hash + 1
# hash ktory zacina 00  - VALID BLOCK

