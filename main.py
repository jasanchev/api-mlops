from fastapi import FastAPI, HTTPException
from simulador import SimuladorEstocastico

app = FastAPI(title="API de Simulación Estocástica")

# 1. Instanciamos el modelo al iniciar el servidor (para no recargarlo en cada petición)
modelo = SimuladorEstocastico()

@app.get("/")
def ruta_principal():
    return {"mensaje": "API del Gemelo Digital operativa"}

# 2. Creamos la ruta web que ejecutará el modelo
@app.get("/simulacion")
def ejecutar_simulacion(estado_inicial: str = "Operativo", ciclos: int = 5):
    
    # Validamos que el usuario no envíe un estado inventado
    if estado_inicial not in modelo.estados:
        raise HTTPException(
            status_code=400, 
            detail=f"Estado '{estado_inicial}' no válido. Opciones: {modelo.estados}"
        )
    
    # Ejecutamos la predicción y la devolvemos
    resultado = modelo.predecir_estado(estado_inicial, ciclos)
    return resultado
