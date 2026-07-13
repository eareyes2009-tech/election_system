import os
import uuid

def registrarse(cuentas):

    usuario = dict.fromkeys(["Nombre", "Contraseña"])
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")

        if nombre != "" and contraseña != "":

            id = uuid.uuid4()
            usuario.update({"ID": id, "Nombre": nombre, "Contraseña": contraseña})

            print("Registro exitoso")
            cuentas.append(usuario)
            os.system('cls')
            break
        else:
            print("Campos invalidos")
            os.system('cls')