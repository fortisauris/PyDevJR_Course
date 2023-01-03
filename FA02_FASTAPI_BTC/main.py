from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI(debug=True)


@app.get('/')
def index():
    return {'msg': 'VSETKO JE OK'}

@app.get('/usd2btc')
def USD_current_price():
    re = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if re.status_code == 200:
        data = re.json()
        print(data)
        return data
