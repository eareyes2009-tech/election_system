def verificar_candidatos(candidatos):
    
    verificacion = False

    if candidatos == []:
        print("No existe candidatos. Registre candidatos primero")
    elif len(candidatos) <= 1:
        print("Candidatos insuficientes para realizar votacion")
    else:
        verificacion = True

    return verificacion

def verificar_votantes(votantes):

    datos_ingresados = dict.fromkeys(["Nombre", "Apellido", "Identidad"])

    while True:

        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        if nombre == "" and apellido == "":
            print("Campos Invalidos")
        else:        
            identidad = input("Ingrese su numero de identidad: ")
            verificacion = verificar_identidad(identidad)
            return verificacion
        
def verificar_identidad(identidad):

    verificacion = list()
    duplicar = False

    for digito in reversed(identidad): 

        digito = int(digito)

        if duplicar == True:
            digito *= 2
            duplicar = False
        else:
            digito *= 1
            duplicar = True

        if digito > 9:

            digito -= 9

        verificacion.append(digito)
        
    suma_total = sum(verificacion) 
    resto = suma_total % 10

    if resto == 0:
        print("Validacion Exitosa")
        validacion = True
    else:
        print("Identidad no Valida")
        validacion = False

    return validacion