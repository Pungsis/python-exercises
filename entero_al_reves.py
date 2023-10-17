
def entero_al_reves(num):

    lista = []
    for i in str(num):
        lista.append(int(i))
    print(lista)
    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            current = lista[i]
            print(current)
            valor = lista[j]

            if lista[i] - lista[j] == 0:
                lista[i] = valor
            elif lista[i] - lista[j] > 0:
                lista[j] = current
                lista[i] = valor
            else:
                lista[i] = current
                lista[j] = valor

    nuevo_texto = ""
    for i in lista:
        nuevo_texto += str(i)
    return int(nuevo_texto)


print(entero_al_reves(1234))
