import pandas as pd
import os

def verify_candidates():
    
    verification = False
    candidates = pd.read_excel("data/candidates/candidates.xlsx")

    if candidates["ID"].tolist() == [] or len(candidates["ID"].tolist()) <= 1:
        pass
    else:
        verification = True

    return verification

def verify_voter():

    verification = False
    voters = pd.read_excel("data/voters/voters.xlsx")

    if (voters["ID"].tolist() == []) or (False not in voters["Estado"].tolist()):
        pass
    else:
        verification = evaluate_voter()

    return verification    
        
def evaluate_voter():

    voters = pd.read_excel("data/voters/voters.xlsx", index_col= False)
    verification = False
    first_name = input("Ingrese su nombre: ")
    last_name = input("Ingrese su apellido: ")

    if first_name == "" or last_name == "":
        print("Campos Invalidos")
        os.system("cls")
    else:        
        identity = input("Ingrese su numero de identidad: ")

        voter_info = voters.loc[(voters["Nombre"] == first_name) & (voters["Apellido"] == last_name) & (voters["Identificacion"].astype(str) == identity)]    

        if not voter_info.empty:
            voter_state = voter_info.iloc[0]["Estado"]

            if voter_state == True:
                print("El elector ya votó")
            else:
                verification = True
                voters.loc[(voters["Nombre"] == first_name) & (voters["Apellido"]==last_name) & (voters["Identificacion"].astype(str) == identity), "Estado"] = True
                with pd.ExcelWriter("data/voters/voters.xlsx") as write:
                   voters.to_excel(write, index = False)
        else:
            print("No existe el elector") 

    return verification

        