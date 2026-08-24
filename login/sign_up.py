import os
import uuid
import bcrypt

def registrarse(cuentas):

    usuario = dict.fromkeys(["Nombre", "Contraseña"])
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")

        if nombre != "" and contraseña != "":

            hash = hash_password(contraseña)
            id = uuid.uuid4()
            usuario.update({"ID": id, "Nombre": nombre, "Contraseña": hash})

            print("Registro exitoso")
            cuentas.append(usuario)
            os.system('cls')
            break
        else:
            print("Campos invalidos")
            os.system('cls')

def hash_password(contraseña):

    bytes = contraseña.encode("utf-8")
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(bytes, salt)

    return password_hashed