import random
limite = random.randint(150, 600)
print("limite ", limite)
promedio = 0
contador = 0
suma = 0
while limite > promedio:
    contador += 1
    numero_random = random.randint(10, 60)
    suma += numero_random
    promedio = promedio + (suma / contador)
    print(f"numero: {numero_random}, suma: {suma} promedio: {promedio} ")
    if (int(promedio) - promedio) == 0:
        print(f"el promedio es un entero: {promedio}")
