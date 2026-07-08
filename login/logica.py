import os
import uuid

def inicio_sesion(cuenta, cuentas):

    datos_ingresados = dict.fromkeys(["Nombre", "Contraseña"])
    contador = 0
    while contador <5 :
        coincidencia = False
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")
        datos_ingresados.update({"Nombre": nombre, "Contraseña": contraseña})

        for usuario in cuentas:
            if datos_ingresados["Nombre"] == usuario["Nombre"] and datos_ingresados["Contraseña"] == usuario["Contraseña"]:
                coincidencia = True
                break
        if coincidencia:
            print("Inicio de sesion exitoso")
            os.system('cls')
            cuenta = asignar_cuenta(cuentas, datos_ingresados)
            return coincidencia, cuenta
        else:
            contador += 1
            print("Usuario o contraseña incorrecta")
            os.system('cls')
    else:
        if contador == 5:
            os.system('cls')
            print("Demasiados intentos incorrectos")
            return False, cuenta

def registrarse(cuentas):

    usuario = dict.fromkeys(["Nombre", "Contraseña"])
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")

        if nombre != "" and contraseña != "":

            id = uuid.uuid4()
            print(type(id))
            usuario.update({"ID": id, "Nombre": nombre, "Contraseña": contraseña})

            print("Registro exitoso")
            cuentas.append(usuario)
            os.system('cls')
            break
        else:
            print("Campos invalidos")
            os.system('cls')

def cerrar_sesion(cuentas,cuenta):

    for seleccion in cuentas:
        if seleccion["ID"] == cuenta["ID"]:
            cuenta.update({"ID" : None, "Nombre" : None, "Contraseña": None})

    return False, cuenta

def asignar_cuenta(cuentas, datos_ingresados):

    for seleccion in cuentas:
        if seleccion["Nombre"] == datos_ingresados["Nombre"] and seleccion["Contraseña"] == datos_ingresados["Contraseña"]:
            cuenta = seleccion.copy()
            return cuenta