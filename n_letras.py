n = (input("ingrese un numero n (natural): "))
letra = input("ingrese una letra n: ")
letra = letra.upper()

print(str(n).find("."))


def contador(letra, lista):
    contador2 = 0
    for i in lista:
        if letra == i:
            contador2 += 1
    return contador2


def imprimir_n_letras():
    if float(n) < 1 or str(n).find(".") > 0:
        return "No es numero natural!"

    lista = []
    if len(letra) > 1:
        for i in letra:
            contador_nuevo = contador(i, letra)
            if contador_nuevo > 1 and i not in lista:
                lista.append(i)

    return lista


print(imprimir_n_letras())
