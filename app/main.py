import os
from app.candidates import registrar_candidato
from app.votes import vote
from app.results import evaluate_votes
from app.voters import voters_registrer

def menu():

    system = True

    while system:
        
        print("Menu Principal")
        print("1.Ingresar Candidato\n"
            "2.Registrar Votante\n"
            "3.Votar\n"
            "4.Ver resultados\n"
            "5.Salir")
        pnt = input("Ingrese la opcion (1-5): ")

        match pnt:

            case "1":
                os.system('cls')
                registrar_candidato()
            case "2":

                os.system('cls')
                voters_registrer()
            case "3":
                os.system('cls')
                vote()

            case "4":
                os.system('cls')
                evaluate_votes()
            case "5":
                os.system('cls')
                sistema = False
            case _:
                  print("¿?")
                  os.system('cls')