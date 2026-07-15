import os
import random

def registrar_candidato(candidatos):

    datos_ingresados = dict.fromkeys(["Nombre", "Apellido", "Partido", "Casilla","Votos"])

    
    while True:

        nombre = input("Ingrese el primer Nombre: ")
        apellido = input("Ingrese el primer Apellido: ")
        partido = input("Ingrese el partido al que pertenece: ")

        if nombre != "" and apellido != "" and partido != "":

            casilla = validacion_casilla(candidatos)
            datos_ingresados.update({"Nombre":nombre,"Apellido":apellido,"Partido":partido,"Casilla": casilla, "Votos": 0})
            print("Registro exitoso")
            candidatos.append(datos_ingresados)
            os.system('cls')
            break
        else:
            print("Campos invalidos")
            os.system('cls')
       
def validacion_casilla(candidatos):

    casilla_libre = False
    casillas_leidas = list()


    while not casilla_libre:
                
        casilla = random.randint(0,100)

        for seleccion in candidatos:

            casillas_leidas.append(seleccion["Casilla"])

        if casilla in casillas_leidas:

            casilla_libre = False
        else: 
            casilla_libre = True

    return casilla



