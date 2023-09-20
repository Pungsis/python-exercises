n = 15
contador_divisores = 0
contador = 0
resultado = 0

for i in range(1, n + 1):
    if n % i == 0:
        contador_divisores += 1
        if contador_divisores <= 5:
            if contador % 2 == 0:
                print(f"1 / {i}")
                resultado += 1 / i
                contador += 1

            else:
                print(f"1 / {i}", "hola")
                resultado -= 1 / i
                contador += 1

print(resultado)
print(1 - 1/2 + 1/3 - 1/4 + 1/6)
