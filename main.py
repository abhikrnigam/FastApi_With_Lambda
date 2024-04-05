from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get('/')
def home():
    return "Abbey Gay Saale!!!"