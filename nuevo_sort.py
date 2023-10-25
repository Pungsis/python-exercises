lista = [192, 28, 818, 234, 28, 998, 28, 34, 9, 86, 655, 877]
nueva = []
mayor = 0
while len(lista) > 0:
    index = 0
    for i in range(0, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            index = i
    lista.pop(index)
    print(lista)
    nueva.append(mayor)
    mayor = 0


print(nueva)
