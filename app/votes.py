import os
from app.verification import verificar_candidatos
from app.verification import verificar_votantes
import pandas as pd

def votar():

    verificacion_candidatos = verificar_candidatos()
    verificacion_votante = verificar_votantes()
    contador = 0

    if verificacion_candidatos and verificacion_votante:

        candidates = pd.read_excel("data/candidates/candidates.xlsx", index_col=False)
        voters = pd.read_excel("data/voters/voters.xlsx", index_col= False)
        print("Candidatos")

        cnt = len(candidates["ID"].tolist()) - 1
        while cnt >= 0:
            
            contador += 1
            print(f"{contador}. Candidato: {candidates.iloc[cnt]["Nombre"]} {candidates.iloc[cnt]["Apellido"]}, Partido: {candidates.iloc[cnt]["Partido"]}, Casilla: {candidates.iloc[cnt]["Casilla"]}")
            cnt -= 1

        voto = int(input(f"¿Cual desea votar? Introduzca el numero de casilla "))
 
        if voto in candidates["Casilla"].tolist():

                candidates.loc[candidates["Casilla"] == voto, "Votos"] += 1 
                with pd.ExcelWriter("data/candidates/candidates.xlsx") as write:
                    candidates.to_excel(write, index = False)

                os.system('cls')