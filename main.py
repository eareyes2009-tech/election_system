import os
import login.logica

def main(sesion, sistema, cuenta): 
    
    if sesion == False:
        print("Inicio")
        print("1.Inicio de Sesion\n"
        "2.Registrarse\n"
        "3.Salir ")
        pnt = input("Ingrese la opcion (1-3): ")

        match pnt:

            case "1":
                os.system('cls')
                sesion, cuenta = login.logica.inicio_sesion(cuenta, cuentas)
                    
            case "2":
                os.system('cls')
                login.logica.registrarse(cuentas)
            case "3":
                os.system('cls')
                sistema = False
            case _:
                print("¿?")
                os.system('cls')
                
    elif sesion == True:
        
        print("Inicio")
        print("1.Ingresar al sistema\n"
            "2.Cerrar Sesion\n"
            "3.Salir ")
        pnt = input("Ingrese la opcion (1-3): ")
        
        match pnt:
            case "1":
                os.system('cls')
                print("Ingresando...")
                sistema = False

            case "2":
                os.system('cls')
                sesion, cuenta = login.logica.cerrar_sesion(cuentas, cuenta)
            case "3":
                os.system('cls')
                sistema = False

            case _:
                print("¿?")
                os.system('cls')
    return sesion, sistema, cuenta

sesion = False
sistema = True
cuentas = []
cuenta = dict.fromkeys(["ID", "Nombre", "Contraseña"])

while sistema == True:
    sesion, sistema, cuenta = main(sesion,sistema, cuenta)
else:
    os.system('cls')