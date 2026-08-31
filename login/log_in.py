import os
import bcrypt
import pandas as pd


def inicio_sesion():

    users = pd.read_excel("data/users/users.xlsx")
    contador = 0
    while contador <5 :
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ").encode("utf-8")

        users_names = users[users["Nombre"] == nombre]
        if not users_names.empty:

            users_password = users_names.iloc[0]["Contraseña"].encode("utf-8")

            if bcrypt.checkpw(contraseña, users_password):

                print("Inicio de sesion exitoso")
                os.system('cls')
                cuenta = asignar_cuenta(users,nombre)
                return True, cuenta
        else:
            contador += 1
            print("Usuario o contraseña incorrecta")
            os.system('cls')
    else:
        if contador == 5:
            os.system('cls')
            print("Demasiados intentos incorrectos")
            return False, None
        
def asignar_cuenta(users,name):

    cuenta = users[users["Nombre"] == name]
    return cuenta.to_dict(orient = "records")