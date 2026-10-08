import pandas as pd
import msvcrt
import os

def evaluate_votes():

        candidates = pd.read_excel("data/candidates/candidates.xlsx")

        winner = candidates.sort_values(by="Votos", ascending=False).head()

        if winner.iloc[0]["Votos"] > winner.iloc[1]["Votos"]:
                print(f"El ganador es {winner.iloc[0]['Nombre']} del partido {winner.iloc[0]['Partido']}") 
                print("\n Presione una tecla para continuar...")
                msvcrt.getch()
                os.system("cls")

        elif winner.iloc[0]["Votos"] == winner.iloc[1]["Votos"]:

                print("Existe un empate entre los candidatos.")
                print("\n Presione una tecla para continuar...")
                msvcrt.getch()
                os.system("cls")