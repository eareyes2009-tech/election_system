import os
from app.verification import verify_candidates
from app.verification import verify_voter
import pandas as pd

def vote():

    candidate_verification = verify_candidates()
    voter_verification = verify_voter()
    counter = 0

    if candidate_verification and voter_verification:

        candidates = pd.read_excel("data/candidates/candidates.xlsx", index_col=False)
        voters = pd.read_excel("data/voters/voters.xlsx", index_col= False)
        print("Candidatos")

        cnt = len(candidates["ID"].tolist()) - 1
        while cnt >= 0:
            
            counter += 1
            print(f"{counter}. Candidato: {candidates.iloc[cnt]["Nombre"]} {candidates.iloc[cnt]["Apellido"]}, Partido: {candidates.iloc[cnt]["Partido"]}, Casilla: {candidates.iloc[cnt]["Casilla"]}")
            cnt -= 1

        user_vote = int(input(f"¿Cual desea votar? Introduzca el numero de casilla "))
 
        if user_vote in candidates["Casilla"].tolist():

                candidates.loc[candidates["Casilla"] == user_vote, "Votos"] += 1 
                with pd.ExcelWriter("data/candidates/candidates.xlsx") as write:
                    candidates.to_excel(write, index = False)
                print("Voto Registrado Exitosamente")
                os.system('cls')
    elif not candidate_verification and voter_verification:
        print("Error: Candidatos No Validos")
    elif not voter_verification and candidate_verification:
         print("Error: Votantes No validos")
    else:
         print("Error: Informacion de Candidatos y Votantes no valida.")