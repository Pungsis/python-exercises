import random
apellido = input("ingrese su apellido por favor: ")
clave = ""

for i in apellido:
    if not i in "aeiouAEIOU":
        if len(clave) < 4:
            clave += i

if len(clave) != 4:
    print("hello!")
    while len(clave) < 4:
        clave += "*"

print(f"su clave es {(clave + str(random.randint(0, 9))).upper()}")
