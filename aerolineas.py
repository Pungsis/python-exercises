aerolinea = input("ingrese la aerolinea: ")

count = 0
abreviatura = ""

for i in aerolinea:
    count += 1
    if aerolinea.find(" ") > 0:
        print("la abreviatura es: ",
              aerolinea[0].upper() + aerolinea[aerolinea.find(" ") + 1].upper())
        break
    if count == 1:
        abreviatura += i
    else:
        if i in "aeiou":
            continue
        else:
            abreviatura += i
            print("la abreviatura es: ",
                  abreviatura.upper())
            break
