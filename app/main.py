import os
from app.candidates import registrar_candidato
from app.votes import votar
from app.results import *


def menu():

    sistema = True

    while sistema:
        print("Menu Principal")
        print("1.Ingresar Candidato\n"
        "2.Votar\n"
        "3.Ver resultados\n"
        "4.Salir")
        pnt = input("Ingrese la opcion (1-4): ")

        match pnt:

            case "1":
                os.system('cls')
                registrar_candidato(candidatos)

            case "2":
                os.system('cls')
                votar(candidatos)

            case "3":
                os.system('cls')
            case "4":
                os.system('cls')
                sistema = False
            case _:
                  print("¿?")
                  os.system('cls')

candidatos = []
