def cerrar_sesion(cuentas,cuenta):

    for seleccion in cuentas:
        if seleccion["ID"] == cuenta["ID"]:
            cuenta.update({"ID" : None, "Nombre" : None, "Contraseña": None})

    return False, cuenta

