'''
SESSION23 - requests, AUTH, Unittesty,
'''

import requests
from requests.auth import AuthBase, HTTPBasicAuth
import getpass
import jwt
from requests_oauthlib import OAuth1Session

# ROZCVICKA

def parne_neparne(n: int):
    '''
    Funkcia skusa ci je cislo parne alebo nie. Ak je parne tak vrati True
    Ak nie vrati False.
    param1::: n- integer
    return::: bool
    '''
    if n/2 == int(n/2):  # 3/2 = 1.5  == int(3/2) = 1
        return True
    else:
        return False

# napisat testy
'''
# ziskaj kolaciky
url = 'https://github.com'
r = requests.get(url)

print(r.cookies)

# posli kolacik
url = 'https://httpbin.org/cookies'
cookies = dict(nase_cookies='working')
r = requests.get(url, cookies=cookies)
print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('chutny_kolacik', 'mnam', domain='httpbin.org', path='/cookies')
jar.set('hnusny_kolacik', 'fuj', domain='httpbin.org', path='/niekde')
r = requests.get('http://httpbin.org', cookies=jar)
print(r.text)

r = requests.get('http://github.com', allow_redirects=True)
print(r.url)
print(r.status_code)
print(r.history)

s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/12345')  # nastvalili a vlozili
r = s.get('https://httpbin.org/cookies')  # vytiahli sme ju zo servera
print(r.text)

s = requests.Session()
s.auth = ('user', 'password')
s.headers.update({'x-test': 'true'})

r = s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)

with requests.Session() as s:
    s.get('https://httpbin.org/cookies/set/sessioncookie/2483278432874732')

r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
print(r.headers)
print(r.request.headers)

s = requests.Session()
data = {'nieco': 'neviemco'}
headers = {'x-test': 'true'}
url = 'https://httpbin.org/post'
req = requests.Request('POST', url, data=data, headers=headers)
pripravevy_request = req.prepare()

pripravevy_request.body = 'TOTO TAM CHCEM VLOZIT'
del pripravevy_request.headers['Content-Type']

resp = s.send(pripravevy_request)
# stream=stream
#verify=verify
#proxies=proxies
#cert=cert
#timeout
print(resp.status_code)

# CERTIFIKATY
# MOJ KLUC(KLIENT)  <---> TVOJ KLUC(BANKOVY SERVER)  CERTIFIKACNA AUTORITA
# Certifikat CA - https://www.tatrabanka.sk  -- TATRABANKA
# Certifikat CA - https://www.tatr.banka.sl  --> HACKER

rq = requests.get('https://en.wikipedia.org', verify=True)  # verifikuje hostov certifikat
print(rq.status_code)

# rq = requests.get('https://en.wikipedia.org', cert=('/cert'))  # TODO verifikuje clientov certifikat
# print(rq.status_code)

with requests.Session() as s:
    s.auth = ('andrej', getpass.getpass())
    response = s.get('https://github.com/user')

print(response.headers)
print(response.text[:100])
# print(response.json())


class TokenAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r
    
r = requests.get('https://httpbin.org/get', auth=TokenAuth('Toto je moj bezpecny token dlhy kilometer'))
print(r.status_code)
print(r.headers)
print(r.text)
'''
# JSON Web Token  - JWT

token = jwt.encode({'some':'JWT'}, 'NASE TAJOMSTVO', algorithm='HS256')
print(token)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoiSldUIn0.CDRclKWGeKTLMqIhyfN1IPfDE20M4zoi_-jyN5C7b_E
# https://jwt.io
verify_token = jwt.decode(token, key='NASE TAJOMSTVO', algorithms=['HS256',])
print(verify_token)
print(jwt.get_unverified_header(token))

# OAuth1
# OAuth

test = OAuth1Session('consumer_key', client_secret='NASE TAJOMSTVO')
url = 'https://github.com/user'
r = test.get(url)
print(r.status_code)
print(r.content)

# TODO Prestavka do 20:15

# UNITTEST

# TODO DOMACA PISAT TESTY