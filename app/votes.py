import os

def votar(candidatos):

    verificacion = verificar_candidatos(candidatos)
    contador = 0

    while verificacion:
        os.system('cls')
       
        print("Candidatos")
        for opcion in candidatos:
            
            contador += 1
            candidato = list(opcion.values())[:-1]
            print(f"{contador}. {candidato}")

        voto = input(f"¿Cual desea votar?(1-{contador})")

        

        break

def verificar_candidatos(candidatos):
    
    verificacion = False

    if candidatos == []:
        print("No existe candidatos. Registre candidatos primero")
    elif len(candidatos) <= 1:
        print("Candidatos insuficientes para realizar votacion")
    else:
        verificacion = True

    return verificacion