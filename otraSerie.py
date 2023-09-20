n = int(input("ingrese un numero natural: "))

contador = 0

if n > 1 or int(n) == float(n):

    for i in range(1, n + 1):
        contador += 1

        if i <= 2:
            print(f"Se suma 1 / 2 a la 1")
        else:
            if i % 4 == 0:
                print(f"Se suma 1 / 2 a la 2")
            else:
                print(f"Se suma 1 / 2 a la 1")
