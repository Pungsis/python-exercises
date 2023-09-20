tarjeta = input("ingrese el numero de tarjeta (deben ser 16 digitos): ")
digitos_a_ocultar = input("ingrese la cantidad de digitos que desea ocultar: ")

count = 0
tarjeta_oculta = ""

for i in tarjeta:
    count += 1
    if count <= int(digitos_a_ocultar):
        tarjeta_oculta += "*"
    else:
        tarjeta_oculta += i


print(tarjeta_oculta)
