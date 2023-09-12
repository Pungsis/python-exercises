n = int(input("ingrese un numero: "))


result = 0
suma = 0
for i in range(1, n):
    result += i
    suma += 1 / result
    print(f"se esta sumando esto: 1 / {result}")

print(suma)
