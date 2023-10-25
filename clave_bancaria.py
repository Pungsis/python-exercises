# dni = input("ingrese su dni por favor: ")
apellido = str(input("ingrese su apellido por favor: "))
clave_cliente = input("Debe generar una clave, ingresela: ")


def excluir(texto, noentexto):
    text = ""
    for i in texto:
        if not i in noentexto:
            text += i
    return text


def verificar_consonantes(clave):
    letras_clave = excluir(clave, "0123456789")

    for i in letras_clave:
        if i in apellido:
            return False

    for i in letras_clave:
        contador = 0
        for j in letras_clave:
            if i == j:
                contador += 1
            if contador > 1:
                return False

    return True


def verificar_numeros(clave):
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    conteo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    clave_solo_numeros = ""
    for i in clave:
        if i in "0123456789":
            clave_solo_numeros += i

    if len(clave_solo_numeros) != 4:
        return False

    for i in clave_solo_numeros:
        if int(i) in numeros:
            conteo[int(i)] += 1

    verificacion_final = True

    for i in conteo:
        if i > 1:
            verificacion_final = False
    return verificacion_final


def verificacion_clave(clave):
    if clave[0] not in "aeiou" and len(clave) >= 5 and len(clave) <= 12 and verificar_consonantes(clave) and verificar_numeros(clave):
        print("Clave cumple los requisitos!")
        return True
    else:
        print("No cumple crack")
        return False


while not verificacion_clave(clave_cliente):
    print(verificacion_clave(clave_cliente))
    apellido = str(input("ingrese su apellido por favor: "))
    clave_cliente = input("Debe generar una clave, ingresela: ")
