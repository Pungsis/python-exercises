from random import randint
import math


def tubo():
    lista = [10, 20, 50]
    return lista[randint(0, 2)]


def ventaDiaria(capacidad):
    return randint(0, capacidad)


unidades = tubo()
costo_inicial = unidades * 16
venta_por_dia = ventaDiaria(unidades)
contador = 0
precio_unitario = 28
total_vendido = 0
while unidades > 0:
    if contador == 0:
        print("precio unitario dia 1: ", round(precio_unitario, 2))
        total_vendido += precio_unitario * venta_por_dia
        print("total vendido: ", total_vendido, "Chocolates restantes: ",
              unidades, "Ventas por dia: ", venta_por_dia)

    else:
        precio_unitario += (1/3) * 28
        print("precio unitario por chocolate dia ",
              contador + 1, " es de ", round(precio_unitario, 2))
        if unidades < venta_por_dia:
            total_vendido += (unidades) * precio_unitario
            print("total vendido: ", total_vendido, "Chocolates restantes: ",
                  (unidades), "Ventas por dia: ", venta_por_dia)
        else:
            total_vendido += (venta_por_dia) * precio_unitario
            print("total vendido: ", total_vendido, "Chocolates restantes: ",
                  unidades, "Ventas por dia: ", venta_por_dia)

    unidades -= venta_por_dia
    contador += 1

print("Los chocolates duraron ", contador, " dias")
print("Ganancia obtenidad: ", total_vendido - costo_inicial)
