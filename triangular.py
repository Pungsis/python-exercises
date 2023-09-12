numero = int(input("ingrese un numero natural: "))

i = 1
secuencia = 0

# Si la condicion es verdadera, el while sigue con la ejecucion
# Cuando es falsa, termina el ciclo
# si el numero es == a la secuencia, entonces es falso que
# numero > secuencia, entonces termina el ciclo while!
# si el numero == secuencia, entonces encontramos que
# el numero es un numero triangular
while numero > secuencia:
    print("loop:", i)
    secuencia = (i * (i + 1)) / 2
    if numero == secuencia:
        print(
            f"el numero que usted ingreso ({numero}) es un numero triangular")
    i += 1

# si el numero es triangular, entonces al terminar el ciclo while
# la secuencia sera igual al numero
# caso contrario, el ciclo while hara un ciclo mas, y terminara
# por que cumple que numero > secuencia, es falso
# entonces sabemos que numero < secuencia, y no encontro
# ninguna igualdad, por lo tanto ese numero no es triangular!

if numero < secuencia:
    print(
        f"el numero que usted ingreso ({numero}) no es un numero triangular")
