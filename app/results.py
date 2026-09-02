import pandas as pd
import msvcrt
import os

def evaluar_votos():

        candidates = pd.read_excel("data/candidates/candidates.xlsx")

        ganador = candidates.sort_values(by="Votos", ascending=False).head()

        if ganador.iloc[0]["Votos"] > ganador.iloc[1]["Votos"]:
                print(f"El ganador es {ganador.iloc[0]['Nombre']} del partido {ganador.iloc[0]['Partido']}") 
                print("\n Presione una tecla para continuar...")
                msvcrt.getch()
                os.system("cls")

        elif ganador.iloc[0]["Votos"] == ganador.iloc[1]["Votos"]:

                print("Existe un empate entre los candidatos.")
                print("\n Presione una tecla para continuar...")
                msvcrt.getch()
                os.system("cls")