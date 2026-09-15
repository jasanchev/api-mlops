from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ruta_principal():
    return {"mensaje": "¡Mi primera API está en línea!"}

@app.get("/prediccion")
def modelo_dummy():
    return {"resultado": 42.5}
