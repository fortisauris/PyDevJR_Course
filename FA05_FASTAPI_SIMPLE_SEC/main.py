from fastapi import FastAPI, Depends, Form
from fastapi_simple_security import api_key_router, api_key_security
import os

app = FastAPI(debug=True)
os.environ['FASTAPI_SECURITY_SECRET'] = 'BRYNDZOVEHALUSKY'  # os.urandom(32)

db = {
    'tajomstvo1': {'heslo k wifi': 'halabala'},
    'tajomstvo2': {'pin ku karte': 1111}
}

'''
@app.post('/login')
def login(username: str = Form(), password: str = Form()):
    return {'username': username, 'password': password}
'''

app.include_router(api_key_router, prefix='/auth', tags=['_auth'])

@app.get('/secured/{tajomstvo}', dependencies=[Depends(api_key_security)])
async def secure_endpoint(tajomstvo: str = None):
    if tajomstvo:
        return db[tajomstvo]
    return {'msg':'Toto je zabezpecena stranka !!!'}

