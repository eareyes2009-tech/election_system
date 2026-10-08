import os
from login.log_in import verify_account
from login.sign_up import register
from login.log_out import close_account
from app.main import menu
from data.management import paths_management


def main(): 

    paths_management()
    system = True
    session = False

    while system:

        if session == False:
            print("Inicio")
            print("1.Inicio de Sesion\n"
            "2.Registrarse\n"
            "3.Salir ")
            pnt = input("Ingrese la opcion (1-3): ")

            match pnt:

                case "1":
                    os.system('cls')
                    session, account = verify_account()

                case "2":
                    os.system('cls')
                    register()
                case "3":
                    os.system('cls')
                    break
                case _:
                    print("¿?")
                    os.system('cls')

        elif session == True:
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
                    session, account = close_account(account)
                case "3":
                    os.system('cls')
                    break

                case _:
                    print("¿?")
                    os.system('cls')

main()