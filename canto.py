def peores_tres_puntuados(lista_participantes, lista_notas):
    for i in range(0, len(lista_participantes)):
        for j in range(0, len(lista_participantes)):
            current = lista_notas[i]
            valor = lista_notas[j]
            current2 = lista_participantes[i]
            valor2 = lista_participantes[j]
            print(lista_notas)

            if lista_notas[i] - lista_notas[j] == 0:
                lista_notas[i] = valor
                lista_participantes[i] = valor2
            elif lista_notas[i] - lista_notas[j] > 0:
                lista_notas[j] = current
                lista_notas[i] = valor
                lista_participantes[j] = current2
                lista_participantes[i] = valor2
            else:
                lista_notas[i] = current
                lista_notas[j] = valor
                lista_participantes[j] = valor2
                lista_participantes[i] = current2

    print(lista_participantes)
    print(lista_notas)
    if len(lista_notas) > 3:
        for i in range(1, 4):
            print(lista_participantes[len(lista_participantes) - i],
                  "Fuera de la competencia con nota: ", lista_notas[len(lista_notas) - i])
    return lista_notas


print(peores_tres_puntuados(["Rodrigo", "Maitena", "Son", "Baby",
      "Perro", "Trasero", "Bony", "Pino"], [9, 3, 2, 6, 7, 53, 43, 145]))
