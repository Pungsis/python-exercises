# ComisionesHabilitadas = [1, 2, 3, 4, 5, 6, 7, 8]
# TurnoDeCadaComision = ["M", "T", "N", "M", "N", "T", "N", "M"]
# CantidadAlumPorComision = [80, 80, 60, 50, 40, 50, 50, 40]


# def comisiones(turno):
#     lista = [[], [], []]
#     for i in range(0, len(ComisionesHabilitadas)):
#         if turno == TurnoDeCadaComision[i]:
#             lista[0].append(TurnoDeCadaComision[i])
#             lista[1].append(ComisionesHabilitadas[i])
#             lista[2].append(CantidadAlumPorComision[i])
#     return lista


# # supongo que la lista de los alumnos inscriptos es igual a la cantidad de comisiones
# def inscripcion(turno, lista_alumnos_asignados):
#     comisionesPorTurno = comisiones(turno)
#     nueva_lista_alumnos_inscriptos = []
#     for i in range(0, len(lista_alumnos_asignados)):
#         alumnosDisponibles = comisionesPorTurno[2][i] - \
#             lista_alumnos_asignados[i]
#         if alumnosDisponibles > 0 and len(nueva_lista_alumnos_inscriptos) < len(comisionesPorTurno[1]):
#             nueva_lista_alumnos_inscriptos.append(
#                 [alumnosDisponibles - 1, comisionesPorTurno[1][i], turno])
#         elif alumnosDisponibles <= 0 and len(nueva_lista_alumnos_inscriptos) < len(comisionesPorTurno[1]):
#             print("comision ", comisionesPorTurno[1][i], " llena")
#             nueva_lista_alumnos_inscriptos.append([0])
#         elif len(nueva_lista_alumnos_inscriptos) == 0:
#             print("Todas las comisiones llenas")
#     return nueva_lista_alumnos_inscriptos

# print(inscripcion("M", [90, 70, 100]))

ComisionesHabilitadas = [1, 2, 3, 4, 5, 6, 7, 8]
TurnoDeCadaComision = ["M", "T", "N", "M", "N", "T", "N", "M"]
CantidadAlumPorComision = [1, 80, 60, 0, 40, 50, 50, 0]
lista_DNIS = [1234, 3833, 9384, 9394, 8382,
              8384, 8384, 9023, 8386, 7123, 2993, 1232]
turno_elegido = ["M", "T", "M", "N", "T", "M", "T", "M", "T", "M", "T", "N"]
lista_alumnos_restantes = [] + CantidadAlumPorComision


def inscripcion(turno):
    operacion = False
    index = 0
    for i in range(0, len(lista_alumnos_restantes)):
        if turno == TurnoDeCadaComision[i] and lista_alumnos_restantes[i] > 0 and operacion == False:
            lista_alumnos_restantes[i] -= 1
            index = i
            operacion = True
    if operacion == False:
        return 0
    return "Comision asignada: " + str(ComisionesHabilitadas[index])


print(inscripcion("M"))


def verificacion_inscripcion(lista_dni, lista_turno):
    for i in range(0, len(lista_dni)):
        mensaje = inscripcion(lista_turno[i])
        if mensaje == 0:
            print(lista_dni[i], "No hay vacante !!!",
                  "Turno: ", lista_turno[i])
        else:
            print(lista_dni[i], mensaje, "Turno: ", lista_turno[i])
    return "Verificacion finalizada"


print(verificacion_inscripcion(lista_DNIS, turno_elegido))
print(lista_alumnos_restantes)
