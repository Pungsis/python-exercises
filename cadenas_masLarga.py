lista_nombres = ["Pepe", "Ana", "Perro",
                 "Pedro", "Petoasd", "peor", "perosads"]


def cadenaMasLarga(lista):
    largo_max = 0
    lista_nueva = []
    for i in lista:
        if len(i) > largo_max:
            largo_max = len(i)

    for j in lista:

        if len(j) == largo_max:
            lista_nueva.append(j)

    return lista_nueva


print(cadenaMasLarga(lista_nombres))
