from random import randint


def enCondiciones(num):
    lista = [True, False]
    return lista[randint(0, 1)]


print(enCondiciones(1000))


def sorteados(list):
    lista = []
    for i in list:
        if enCondiciones(i) and len(lista) < 3:
            lista.append(i)
    return lista


def suscriptores():
    lista = []
    for i in range(0, 85):
        lista.append(randint(1000, 2000))
    return lista


ganadores = sorteados(suscriptores())

for i in ganadores:
    print("plan numero ", i, " fue sorteado!")
