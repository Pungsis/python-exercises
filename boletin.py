titulo = input("ingrese el titulo: ")
tipo = input("ingrese el tipo: ")
materia = input("ingrese la materia: ")

titulo_modificado = ""
palabra = ""
count = 0
for i in titulo:
    palabra += i
    count += 1
    if i == " " or count == len(titulo):
        palabra = palabra[:len(palabra)]
        if len(palabra) <= 4:
            palabra = ""
        else:
            if len(titulo_modificado) == 6:
                break
            titulo_modificado += palabra[0].upper() + palabra[1:3]
            palabra = ""

print(titulo_modificado)


print("el codigo generado es: ",
      tipo[:3].upper() + "-" + materia[0::len(materia) - 1] + "/" + titulo_modificado)
