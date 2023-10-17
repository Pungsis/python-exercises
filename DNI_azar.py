lista_DNI = [1611, 1688, 2659, 1613, 1613, 1628, 1562, 1111, 1613, 1658]
lista_NOMBRES = ["Lorena", "Fernando", "Mariana", "Maximo",
                 "Daniel", "Ariel", "Cristina", "Santiago", "Carlos", "Ivan"]
lista_APELLIDOS = ["Perez", "Espisona", "Naniz", "Fernandez",
                   "Lancha", "Negro", "Vholve", "Father", "Enrique", "Yeoman"]
lista_EDAD = [1, 23, 11, 58, 74, 6, 42, 99, 28, 63]


def encontrar_indice_dni(dni):
    indice = None
    for i in range(0, len(lista_DNI) - 1):
        if lista_DNI[i] == dni:
            indice = i
    return indice


def aptitud_dni(dni):
    indice = encontrar_indice_dni(dni)
    if indice == None:
        return "DNI INVALIDO"
    if lista_EDAD[indice] <= 16:
        return "DNI: " + str(dni) + " *menor* " + lista_APELLIDOS[indice] + " ," + lista_NOMBRES[indice]
    elif lista_EDAD[indice] >= 65:
        return "DNI: " + str(dni) + " *no Apto* " + lista_APELLIDOS[indice] + " ," + lista_NOMBRES[indice]

    return "DNI: " + str(dni) + " *a sorteo* " + lista_APELLIDOS[indice] + " ," + lista_NOMBRES[indice]


print(aptitud_dni(1232))
