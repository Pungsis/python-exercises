lista = [1, 2, -4, 4, 0, 9, 6, -5, 2, 3, 5, -1, 1, 3]


def listaModificada(list):
    for i in range(0, len(list)):
        if i % 4 == 0:
            list[i] = list[i] * 2
    return list


print(lista)
print(listaModificada(lista))
