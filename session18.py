# AHOJTE VSETCI CO VIETE POUZIVAT GIT PULL

'''

C O M P R E H E N S I O N S   L I S T   A N D   D I C T

'''

#  K L A S I K A

zoznam = list()  # []
for i in range(6):
    zoznam.append(i*3.14)
print(zoznam)

#  M O D E R N A

zoznam = [i*3.14 for i in range(6) if i*3.14 != 0]   # [hodnota cyklus/iteracia filter]
print(zoznam)

meno = 'Milan'

slovnik = {x:meno[x] for x in range(len(meno))}
print(slovnik)
print(slovnik[3])
print(slovnik.keys(), slovnik.values())


import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# BATCH PROCESSING

def compress_image(odkial: str, kam: str):  # filename_w_path
    with Image.open(odkial) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(kam, 'jpeg', optimize=True, quality=50)

# POMOCOU OS.WALK() PREHLIADAT DISK

def get_jpegs(path: str):
    result = []
    raw = os.walk(top=path)
    for root, dirs, files in raw:
        # print(root,dirs,files)
        for file in files:
            # print(file[-4:])
            if file[-4:] == '.jpg' or file[-4:] == 'jpeg':
                result.append(root + '/' + file)
    return result


# METADATA FOTOGRAFIE SU TZV EXIF DATA

def get_exif(file_w_path: str):
    i = Image.open(file_w_path)
    info = i.getexif()
    print(info)
    exif_data = {TAGS.get(tag): value for tag, value in info.items()}
    print(exif_data)




if __name__ == '__main__':
    compress_image('coder.jpg', 'coder3.jpg')
    get_jpegs(r"C:\Users\andrejli\PycharmProjects\CestaNaJupyter")
    get_exif(r'C:\Users\andrejli\PycharmProjects\CestaNaJupyter\coder.jpg')

# TODO Dokoncit Kradosa EXIFOV



import base64

text = bytes('Nejaky text', encoding='utf8')
print(text)
encoded_text = base64.b64encode(text)
print(encoded_text)

decoded_text = base64.b64decode(encoded_text, validate=True)
print(decoded_text)


# TODO Prestavka do 20:10

url = base64.urlsafe_b64encode(b'HELLO')
decoded = base64.urlsafe_b64decode(url)
print(url)
print(decoded)

# KNOWN SECRET  - SPOLOCNE TAJOMSTVO - POSUN, HESLO, KLUC,

# DIFFIE HELLMAN ALGORITMUS NA VYMENU KLUCOV
# SYMETRICKE SIFROVANIE

# ASYMETRICKE SIFROVANIE -

# ALICA
AlicineTajomstvo = 547665

# ROBERT
RobertoveTajomstvo = 657587

# Server
g = 45874238949  # nahodne cislo s vysokou entropiou
n = 911  # prvocislo

# Alica ide poslat Robertovi kluc
A_posiela = (g ** AlicineTajomstvo) % n
print('ALICA_POSIELA :', A_posiela)

# Robert poslat Alici kluc
R_posiela = (g ** RobertoveTajomstvo) % n
print('ROBERT POSIELA :', R_posiela)

# Alica otvara Robertov kluc
Robertov_kluc = (R_posiela ** AlicineTajomstvo) % n
print('Robertov zdielany kluc :', Robertov_kluc)

# Robert otvara Alicin kluc
Alicin_kluc = (A_posiela ** RobertoveTajomstvo) % n
print('Alicin zdielany kluc :', Alicin_kluc)
