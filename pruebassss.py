frutas = ["Naranja", "Naranja", "Manzana", "Manzana", "Naranja", "Pera"]

lista = []
lista2 = []

for i in frutas:
    if not i in lista:
        lista.append(i)
        lista2.append([i, 0])

for i in frutas:
    for j in range(0, len(lista2)):
        if i == lista2[j][0]:
            lista2[j][1] += 1

print(lista2)
print("el primer numero que salio fue el %d y en la lista hay %d numeros mayores a %d" % (10, 25, 23))
colores = [1, 3, 4, 5]
colores.pop(2)
print(colores)

print([9] + [] + [7])

listasss = [1, 2, 3, 4, 5, 6, 7]
print(listasss[-1::-1])
