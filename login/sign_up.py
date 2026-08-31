import os
import uuid
import bcrypt
import openpyxl

def registrarse():

    wb = openpyxl.load_workbook("data/users/users.xlsx")
    ws = wb.active
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = bcrypt.hashpw(input("Ingrese una contraseña: ").encode("utf-8"), bcrypt.gensalt())

        if nombre != "" and contraseña != "":

            id = str(uuid.uuid4())
            
            usuario = [id, nombre, contraseña]
            ws.append(usuario)
            print("Registro exitoso")
            os.system('cls')
            break
        else:
            print("Campos invalidos")
            os.system('cls')
    wb.save("data/users/users.xlsx")
    wb.close()