from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator
from typing import Optional

app = FastAPI(debug=True)

class Message(BaseModel):
    msg: str
    code: int
    detail: Optional[str] = 'ZIADNE DALSIE PODROBNOSTI'

    @validator('code')
    def cislo_kodu(cls, v):
        if v in [100,200,300,400,500]:
            return v
        else:
            raise ValueError('Ups tento kod nepoznam')

poziadavky=[]

msgs = {
    200: {'msg': 'VSETKO V PORIADKU', 'code': 200},
    500: {'msg': 'NIECO SA POKAZILO', 'code': 500, 'detail': 'volaj admina'},
    600: {'msg': 'VSETKO SA POKAZILO', 'code': 600, 'detail': 'volaj okamzite admina'},
}

STATUS = msgs[500]

@app.get('/', response_model=Message)
def get_status(q: str = None):
    if q:
        for i in q.split(','):
            print(i)
            poziadavky.append(i)
    return STATUS

@app.get('/poziadavky')
def get_poziadavky():

    return {'poziadavky': poziadavky}