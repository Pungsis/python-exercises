frase = "un lunes lluvioso"


contador = 0

vocales = "aeiouAEIOU"
nueva_frase = ""
palabra_actual = ""
vocales_acumuladas = ""
consonantes_acumuladas = ""

for i in frase:
    contador += 1
    palabra_actual += i

    if i == " " or contador == len(frase):
        for j in palabra_actual:
            if not j in vocales and j != " ":
                consonantes_acumuladas += j
            elif j in vocales and j != " ":
                vocales_acumuladas += j
        nueva_frase += consonantes_acumuladas + vocales_acumuladas + " "
        palabra_actual = ""
        vocales_acumuladas = ""
        consonantes_acumuladas = ""
        print(nueva_frase)
