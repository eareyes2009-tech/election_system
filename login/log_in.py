import os
import bcrypt
import pandas as pd

def verify_account():

    users = pd.read_excel("data/users/users.xlsx")
    attemps = 0
    while attemps <5 :
        name = input("Ingrese nombre de usuario: ")
        password = input("Ingrese una contraseña: ").encode("utf-8")

        users_names = users[users["Nombre"] == name]
        if not users_names.empty:

            users_password = users_names.iloc[0]["Contraseña"].encode("utf-8")

            if bcrypt.checkpw(password, users_password):

                print("Inicio de sesion exitoso")
                os.system('cls')
                account = assign_account(users,name)
                return True, account
        else:
            attemps += 1
            print("Usuario o contraseña incorrecta")
            os.system('cls')
    else:
        if attemps == 5:
            os.system('cls')
            print("Demasiados intentos incorrectos")
            return False, None
        
def assign_account(users,name):

    account = users[users["Nombre"] == name]
    return account.to_dict(orient = "records")