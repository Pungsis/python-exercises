import math
LDiam = [6, 10, 12, 15, 25, 100]
LLargo = [6000, 6000, 4000, 5000, 3000, 2000]
LCant = [10, 2, 8, 10, 1, 1]

peso = "pi*diam*diam/4*largo/1000000*2.71 en kg"

suma_peso = 0
for i in range(0, len(LCant)):
    nuevo_peso = math.pi * LDiam[i] * \
        (LDiam[i] / 4) * (LLargo[i] / 1000000) * 2.71
    suma_peso += nuevo_peso

print("el peso total del deposito es de ", suma_peso, " kg")
