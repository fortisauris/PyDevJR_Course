import fastapi
import uvicorn

app = fastapi.FastAPI(debug=True)


@app.get('/')
def index():
    return {'return': 'Hello'}

@app.get('/cosmic1/{vaha}')  # vaha je v kg
def kalkulacia(vaha: float):
    return {'cena na orbit': (vaha * 1800)}



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)