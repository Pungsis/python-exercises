def lista_decimal(lista, decimal):
    suma = 0
    contador = 0
    lista2 = []
    for i in lista:
        if i % 2 == 0:
            suma += i
            contador += 1
            if len(lista2) < 1 and (suma / contador) >= decimal:
                lista2.append(suma / contador)

    if len(lista2):
        return lista2[0]
    else:
        return "No se llego a ningun promedio que sea mayor al decimal que paso"


print(lista_decimal([2, 3, 4, 5, 6, 8, 9, 2, 3, 5, 10, 20], 7.5))
