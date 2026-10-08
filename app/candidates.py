import os
import random
import openpyxl
import pandas as pd
import uuid

def candidates_register():

    wb = openpyxl.load_workbook("data/candidates/candidates.xlsx")
    ws = wb.active
    candidates = pd.read_excel("data/candidates/candidates.xlsx")
    while True:

        first_name = input("Ingrese el primer Nombre: ")
        last_name = input("Ingrese el primer Apellido: ")
        party = input("Ingrese el partido al que pertenece: ")

        if first_name != "" and last_name != "" and party != "":

            box = box_validation(candidates)
            votes = 0
            id = str(uuid.uuid4())
            cdt = [id, first_name, last_name, party, box, votes]
            print("Registro exitoso")
            ws.append(cdt)
            os.system('cls')
            break
        else:
            print("Campos invalidos")
            os.system('cls')
    wb.save("data/candidates/candidates.xlsx")
    wb.close()

def box_validation(candidates):

    unchecked_box = False
    
    while not unchecked_box:

        found = False
        box = random.randint(0,100)

        for selection in candidates["Casilla"].tolist():

            if box == selection:

                found = True
                break

        if found == False:

            unchecked_box = True

    return box


