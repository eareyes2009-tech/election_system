import os
import random
import openpyxl
import pandas as pd
import uuid

def registrar_candidato():

    wb = openpyxl.load_workbook("data/candidates/candidates.xlsx")
    ws = wb.active
    candidates = pd.read_excel("data/candidates/candidates.xlsx")
    while True:

        nombre = input("Ingrese el primer Nombre: ")
        apellido = input("Ingrese el primer Apellido: ")
        partido = input("Ingrese el partido al que pertenece: ")

        if nombre != "" and apellido != "" and partido != "":

            casilla = validacion_casilla(candidates)
            votos = 0
            id = str(uuid.uuid4())
            cdt = [id, nombre, apellido, partido, casilla, votos]
            print("Registro exitoso")
            ws.append(cdt)
            os.system('cls')
            break
        else:
            print("Campos invalidos")
            os.system('cls')
    wb.save("data/candidates/candidates.xlsx")
    wb.close()

def validacion_casilla(candidatos):

    casilla_libre = False
    
    while not casilla_libre:

        encontrado = False
        casilla = random.randint(0,100)

        for seleccion in candidatos["Casilla"].tolist():

            if casilla == seleccion:

                encontrado = True
                break

        if encontrado == False:

            casilla_libre = True

    return casilla


