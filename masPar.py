entero = int(input("ingrese un numero entero: "))

suma_divisores_pares = 0
suma_divisores_impares = 0

for i in range(1, entero):
    if entero % i == 0 and i % 2 == 0:
        suma_divisores_pares += i
    elif entero % i == 0 and i % 2 != 0:
        suma_divisores_impares += i

# HACER LA SUMA Y COMPARAR! SI LA SUMA DE LOS

print(suma_divisores_pares, suma_divisores_impares)

if suma_divisores_pares > suma_divisores_impares:
    print("El numero que ingreso es MasPar")
else:
    print("El numero que ingreso no es MasPar")
