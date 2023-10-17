import random


def esPrimo(num):
    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False


def listaDeImpares(num1, num2):
    lista = []

    for i in range(num1, num2 + 1):
        if not i % 2 == 0:
            lista.append(i)

    return lista


def listaDePrimos(num1, num2):
    lista = []

    for i in range(num1, num2 + 1):
        if esPrimo(i):
            lista.append(i)
    return lista


def generador_de_listas():
    lista = []
    lista_primos_de_3_a_99 = listaDePrimos(3, 999)
    lista_impares_de_3_a_99 = listaDeImpares(3, 999)

    for i in range(0, 10):
        if i == 0:
            lista.append(lista_impares_de_3_a_99[random.randint(
                0, len(lista_impares_de_3_a_99) - 1)])
        else:
            if not i % 2 == 0:
                lista.append(lista_primos_de_3_a_99[random.randint(
                    0, len(lista_primos_de_3_a_99) - 1)])
            else:
                lista.append(lista_impares_de_3_a_99[random.randint(
                    0, len(lista_impares_de_3_a_99) - 1)])

    return lista


print(generador_de_listas())
print(esPrimo(727), esPrimo(613), esPrimo(499), esPrimo(659), esPrimo(593))
