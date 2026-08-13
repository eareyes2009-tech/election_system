import os
from app.verification import verificar_candidatos
from app.verification import verificar_votantes

def votar(candidatos):

    verificacion_candidatos = verificar_candidatos(candidatos)
    verificacion_votante = verificar_votantes()
    contador = 0

    while verificacion_candidatos and verificacion_votante:
        os.system('cls')
       
        print("Candidatos")
        for opcion in candidatos:
            
            contador += 1
            candidato = list(opcion.values())[:-1]
            print(f"{contador}. Candidato: {candidato[0]} {candidato[1]}, Partido: {candidato[2]}, Casilla: {candidato[3]}")

        voto = int(input(f"¿Cual desea votar? Introduzca el numero de casilla "))

        for seleccion in candidatos:
            
            if voto in seleccion.values():

                seleccion["Votos"] += 1
                os.system('cls')
        
        break