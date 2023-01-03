from fastapi import FastAPI, HTTPException, status
import uvicorn
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


app = FastAPI(debug=True)

auta_db = {
    'Octavia':{'typ':'Octavia', 'vyrobca': 'Skoda', 'datum_vyroby': '1998-10-04', 'miesto': 'Malacky'},
    'A4quattro':{'typ':'A4quattro', 'vyrobca': 'Audi', 'datum_vyroby': '2005-10-04', 'miesto': 'Kosice'},
    'E230':{'typ':'E230', 'vyrobca': 'Mercedes', 'datum_vyroby': '2003-10-04', 'miesto': 'Trencin'}
}

# M O D E L S
class Auto(BaseModel):
    nazov: str = Field(min_length=3, max_length=20)
    vyrobca: Optional[str] = None
    datum_vyroby: date
    miesto: str

class AutoNew(Auto):
    palivo: str = Field(min_length=6)
    farba: Optional[str] = 'cierna'

def check_if_auto_existuje(auto: str):
    if auto not in auta_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='AUTO NEJESTVUJE')

# V I E W S
@app.get('/')
def index():
    # code
    return {'msg': 200}


@app.get('/auta')
def zoznam_aut(q: str = None, limit: int = 20):
    if q:
        result = list()
        for a in auta_db.keys():
            print(auta_db[a].values())
            if q in auta_db[a].values():
                result.append(auta_db[a])
        return result[:limit]
    else:
        zoznam = list(auta_db.values())
        return zoznam[:limit]


@app.get('/auta/{auto}')
def get_auto(auto: str):
    try:
        return auta_db[auto]
    except KeyError:
        raise HTTPException(status_code=404, detail=f'AUTO {auto} SA NENASLO')

@app.post('/auta')
def create_auto(auto: AutoNew):
    nazov = auto.nazov
    # check_if_auto_existuje(nazov)
    auta_db[nazov] = auto.dict()
    return {'msg': f'Auto {nazov} bolo pridane do databazy.'}

@app.delete('/auta/{auto}')
def vymaz_auto(auto: str):
    check_if_auto_existuje(auto)
    del auta_db[auto]
    return {'msg': f'Auto {auto} bolo vymazane z databazy'}

@app.put('/auta')
def update_auto(auto: AutoNew):
    '''
    blah blah blah
    :param auto:
    :return:
    '''
    nazov = auto.nazov
    check_if_auto_existuje(nazov)
    auta_db[nazov] = auto.dict()
    return {'msg': f'Auto {nazov} bolo pozmenene'}

@app.patch('/auta')
def patch_auto(auto: AutoNew):
    nazov = auto.nazov
    check_if_auto_existuje(nazov)
    print(type(auto.dict(exclude_unset=True)))
    prepared_auto = auto.dict(exclude_unset=True)
    auta_db[nazov].update(prepared_auto)
    return {'msg': f'Auto {nazov} bolo patchnute'}


if __name__== '__main__':
    uvicorn.run(app)

# PRestavka do 20:11