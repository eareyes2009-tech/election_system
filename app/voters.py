import pandas as pd
import openpyxl
import uuid
import os

def voters_registrer():

    wb = openpyxl.load_workbook("data/voters/voters.xlsx")
    ws = wb.active
    voters = pd.read_excel("data/voters/voters.xlsx", index_col= False, dtype={"Identificacion" : str})

    while True:

        first_name = input("Ingrese su nombre: ")
        last_name = input("Ingrese su apellido: ")

        if first_name == "" or last_name == "":
            print("Campos Invalidos")
            os.system("cls")
        else:        
            identity = input("Ingrese su numero de identidad: ")
            if validate_identity(identity) and identity not in voters["Identificacion"].tolist():

                state = False
                id = str(uuid.uuid4())

                voter = [id,first_name,last_name,identity,state]

                ws.append(voter)
                wb.save("data/voters/voters.xlsx")
                wb.close
                os.system('cls')
                break
            else:
                print("Identidad no valida")    
                os.system("cls")    
        
def validate_identity(identity):

    verification = list()
    duplicate = False

    for digit in reversed(identity): 

        digit = int(digit)

        if duplicate == True:
            digit *= 2
            duplicate = False
        else:
            digit *= 1
            duplicate = True

        if digit > 9:

            digit -= 9

        verification.append(digit)
        
    total_amount = sum(verification) 
    rest = total_amount % 10

    if rest == 0:
        validation = True
    else:
        validation = False

    return validation