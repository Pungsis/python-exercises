import random

numero = int(input("ingrese un numero: "))

contador_impar = 1
contador = 0
resultado = 0
while resultado < numero:
    contador += 1
    resultado += random.randint(1, 9) / contador_impar
    contador_impar += 2
print(
    f"el resultado final fue {resultado} e hizo falta {contador} terminos de serie")
