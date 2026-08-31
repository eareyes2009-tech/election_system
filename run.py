import os
from login.log_in import inicio_sesion
from login.sign_up import registrarse
from login.log_out import cerrar_sesion
from app.main import menu
from data.management import paths_management


def main(): 

    paths_management()
    sistema = True
    sesion = False

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
                    sesion, cuenta = inicio_sesion()

                case "2":
                    os.system('cls')
                    registrarse()
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
                    sesion, cuenta = cerrar_sesion(cuenta)
                case "3":
                    os.system('cls')
                    break

                case _:
                    print("¿?")
                    os.system('cls')

main()