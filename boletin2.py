titulo = "Negaciones productivas"
tipo = "boletin"
materia = "historia"

contador = 0

codigo = ""

for i in tipo:
    if contador < 3:
        codigo += i.upper()
    contador += 1

codigo += "-"

contador = 0
for i in materia:
    if contador == 0:
        codigo += i
    elif contador == len(materia) - 1:
        codigo += i
    contador += 1

codigo += "/"
print(codigo)

contador = 0
contador2 = 0
palabra_actual = ""
for i in titulo:
    palabra_actual += i
    contador += 1
    if i == " " or contador == len(titulo):
        if len(palabra_actual) <= 4:
            palabra_actual = ""
        else:
            palabra_actual = palabra_actual.capitalize()
            print(palabra_actual)
            for j in palabra_actual:
                if contador2 < 3:
                    codigo += j
                contador2 += 1
            palabra_actual = ""
            contador2 = 0

print(codigo)
