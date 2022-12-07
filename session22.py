'''

SESSION 22 - requests - basic, unittest, QuasiDes cast 2

'''

# Odpocet startu rakety - R O Z C V I C K A


import requests
from getpass import getpass, getuser

rq1 = requests.get('https://api.github.com')
print(rq1.status_code)

if rq1.status_code == 200:
    print('SUCCESS !')
elif rq1.status_code == 404:
    print('NOT FOUND !')

if rq1:
    print(':)')
else:
    print(':(')

print('\n\nCONTENT IN BYTES:\n', rq1.content)
print('\n\nTEXT:\n', rq1.text)
print('\n\nENCODING:\n', rq1.encoding)

print('\nJSON : \n', rq1.json())
print('\nHEADERS : \n', rq1.headers)


def vytlac_hlavicku(rq):
    print('\nHLAVICKA :\n\n')
    for key in rq.headers.keys():
        print(key, '\t', rq.headers[key])
    return True


rq2 = requests.get('https://api.github.com/search/repositories', params=b'q=requests+languague:python')
print(rq2.status_code)
vytlac_hlavicku(rq2)

def google_search(query):
    with requests.session() as c:
        url = 'https://www.google.com'
        query = {'q': query, 'gl':'sk', 'hl':'sk'}
        urllink = requests.get(url, params=query)
        print('LINK : \t', urllink.url)
        print('STATUS : \t', urllink.status_code)
        vytlac_hlavicku(urllink)
    return urllink.text

# obsah = google_search('bryndza')
# print(obsah)


rq3 = requests.head('https://httpbin.org/get')
print(rq3.status_code)
vytlac_hlavicku(rq3)

rq3 = requests.post('https://httpbin.org/post', json={'key':'value'})
print(rq3.status_code)
# print(rq3.json())
print(vytlac_hlavicku(rq3))

# pozriet do requestu
print(rq3.request.url)
print(rq3.request.body)
print(rq3.request)

# rq4 = requests.get('https://api.github.com/user', auth=('user', getpass()))
#print(rq4.status_code)

# pwd = getpass()  # input()
usr = getuser()  #
# print(usr, '\t', pwd)


with open('README.md', 'rb') as f:
    r = requests.post('https://httpbin.org/post', files={'README.md': f})
    print(r.status_code)

'''
UNITTEST - testovaci framework

'''

def give_me_five():

    def set_status():
        return True

    global status
    status = set_status()
    return 5

def get_status():
    global status
    print(status)
    return status

# TODO Domaca uloha spravit jednu funkciu a otestovat pomocou pytestu alebo unittestu