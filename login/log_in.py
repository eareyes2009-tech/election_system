import os

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
        
def asignar_cuenta(cuentas, datos_ingresados):

    for seleccion in cuentas:
        if seleccion["Nombre"] == datos_ingresados["Nombre"] and seleccion["Contraseña"] == datos_ingresados["Contraseña"]:
            cuenta = seleccion.copy()
            return cuenta