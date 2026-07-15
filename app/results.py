import os

def evaluar_votos(candidatos):

        ganador = max(candidatos, key= lambda candidato: candidato["Votos"])

        print(f"El ganador es {ganador["Nombre"]} del partido {ganador["Partido"]}") 