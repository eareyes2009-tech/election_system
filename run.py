import os
from login.log_in import inicio_sesion
from login.sign_up import registrarse
from login.log_out import cerrar_sesion
from app.main import menu

def main(): 

    sistema = True
    sesion = False
    cuentas = []
    cuenta = dict.fromkeys(["ID", "Nombre", "Contraseña"])

    while sistema:

        if sesion == False:
            print("Inicio")
            print("1.Inicio de Sesion\n"
            "2.Registrarse\n"
            "3.Salir ")
            pnt = input("Ingrese la opcion (1-3): ")

            match pnt:

                case "1":
                    os.system('cls')
                    sesion, cuenta = inicio_sesion(cuenta, cuentas)

                case "2":
                    os.system('cls')
                    registrarse(cuentas)
                case "3":
                    os.system('cls')
                    break
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
                    menu()

                case "2":
                    os.system('cls')
                    sesion, cuenta = cerrar_sesion(cuentas, cuenta)
                case "3":
                    os.system('cls')
                    break

                case _:
                    print("¿?")
                    os.system('cls')

main()