calle = "avenida averilio perro tu hermana 1234 6to b 1456 cordoba"

contador = 0
direccion_transformada = ""
texto_actual = ""

for i in calle:
    texto_actual += i

    if i == " " or contador + 1 == len(calle):
        if texto_actual == "avenida ":
            direccion_transformada += "Av. "
            texto_actual = ""
        elif texto_actual == "caba":
            direccion_transformada += "CABA"
            texto_actual = ""
        else:
            direccion_transformada += texto_actual.capitalize()
            texto_actual = ""
    contador += 1

print(direccion_transformada)
