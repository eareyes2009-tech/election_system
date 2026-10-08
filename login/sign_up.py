import os
import uuid
import bcrypt
import openpyxl
import pandas as pd

def register():

    wb = openpyxl.load_workbook("data/users/users.xlsx")
    ws = wb.active
    while True:
        name = input("Ingrese nombre de usuario: ")
        password = bcrypt.hashpw(input("Ingrese una contraseña: ").encode("utf-8"), bcrypt.gensalt())

        if name != "" and password != "":

            if username_validation(name):

                id = str(uuid.uuid4())
            
                user = [id, name, password]
                ws.append(user)
                print("Registro exitoso")
                os.system('cls')
                break   
            else:
                print("Nombre de usuario ya tomado")
                os.system('cls')
        else:
            print("Campos invalidos")
            os.system('cls')
    wb.save("data/users/users.xlsx")
    wb.close()

def username_validation(name):

    users = pd.read_excel("data/users/users.xlsx")

    if name in users["Nombre"].tolist():

        return False
    else:

        return True