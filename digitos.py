numero = None

for i in range(0, 10):
    for j in range(0, 10):
        numero = str(514) + str(i) + str(j)
        numero = int(numero)
        if numero % 8 == 0 and numero % 9 == 0:
            print(
                f"el numero {numero} con x={i} y y={j} es divisible por 8 y 9")
