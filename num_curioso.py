
def es_Curioso(num):

    numTexto = str(num)
    numTextoCuadrado = str(num * num)

    if numTextoCuadrado[-len(numTexto):] == numTexto:
        return True
    return False


print(es_Curioso(6))
print("n    n^2     curiosidad")
lista = []
current = 0
while len(lista) < 10:
    current += 1
    if es_Curioso(current):
        lista.append(current)
        print(current, "    ", current * current, "    ", current)
