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

        if first_name == "" and last_name == "":
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

    verificacion = list()
    duplicar = False

    for digito in reversed(identity): 

        digito = int(digito)

        if duplicar == True:
            digito *= 2
            duplicar = False
        else:
            digito *= 1
            duplicar = True

        if digito > 9:

            digito -= 9

        verificacion.append(digito)
        
    suma_total = sum(verificacion) 
    resto = suma_total % 10

    if resto == 0:
        validacion = True
    else:
        validacion = False

    return validacion