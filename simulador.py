import random

class SimuladorEstocastico:
    def __init__(self):
        # Estados posibles de una máquina (base para un gemelo digital)
        self.estados = ["Operativo", "Mantenimiento", "Fallo"]
        
        # Matriz de transición de probabilidades (Cadenas de Markov)
        self.probabilidades = {
            "Operativo": [0.8, 0.15, 0.05],
            "Mantenimiento": [0.6, 0.3, 0.1],
            "Fallo": [1.0, 0.0, 0.0] # Si falla, se repara y vuelve a estar operativo
        }

    def predecir_estado(self, estado_inicial: str, ciclos: int) -> dict:
        estado_actual = estado_inicial
        historial = [estado_actual]

        # Simulación por eventos discretos paso a paso
        for _ in range(ciclos):
            if estado_actual not in self.estados:
                return {"error": "Estado inicial no válido"}
                
            probs = self.probabilidades[estado_actual]
            estado_actual = random.choices(self.estados, weights=probs)[0]
            historial.append(estado_actual)

        # Devolvemos un diccionario, que FastAPI convertirá automáticamente a JSON
        return {
            "estado_inicial": estado_inicial,
            "ciclos_simulados": ciclos,
            "estado_final": estado_actual,
            "historial_transiciones": historial
        }

# Bloque de prueba: esto solo se ejecuta si corremos este archivo directamente
if __name__ == "__main__":
    sim = SimuladorEstocastico()
    resultado = sim.predecir_estado("Operativo", 5)
    print("Prueba del modelo estocástico:", resultado)
