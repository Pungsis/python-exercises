import random

frase = "Caracoles desafiantes e irrespetuosos!"

contador = 0
consonantes_acumuladas = ""
vocales_acumuladas = ""
print(len(frase))
nueva_frase = ""
palabra_actual = ""

for i in frase:
    palabra_actual += i

    contador += 1
    if i == " " or contador == len(frase):
        print(palabra_actual)
        for j in palabra_actual:

            if not j in "aeiouAEIOU" and j != " ":
                consonantes_acumuladas = j.lower() + consonantes_acumuladas
            elif j in "aeiouAEIOU" and j != " ":
                vocales_acumuladas += j.upper()
        nueva_frase += consonantes_acumuladas + vocales_acumuladas + str(random.randint(10, 99)) + \
            " "
        print(nueva_frase)
        palabra_actual = ""
        consonantes_acumuladas = ""
        vocales_acumuladas = ""

print(contador)
