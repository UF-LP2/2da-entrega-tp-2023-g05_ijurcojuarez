from Cronometro import minutos_transcurridos

enfermeros: int
pacientes = []
medicos: int    # infinitos


def asignar_enfermeros():
    if minutos_transcurridos() == 1380:  # minutos de 23 horas
        enfermeros = 1

    if minutos_transcurridos() == 360:  # minutos de 6 horas
        enfermeros = 2

    if minutos_transcurridos() == 600:  # minutos de 10 horas
        enfermeros = 5

    if minutos_transcurridos() == 960:  # minutos de 16 horas
        enfermeros = 3


def asignar_gravedad(pacientes):
    for i in range(len(pacientes)):
        if pacientes[i]["síntomas"] == 'politraumatismo grave':
            pacientes["gravedad"] = 5    # rojo

        elif pacientes[i]["síntomas"] == 'coma' or pacientes[i]["síntomas"] == 'convulsiones' or pacientes[i]["síntomas"] == 'hemorragia digestiva' or pacientes[i]["síntomas"] == 'isquemia':
            pacientes[i]["gravedad"] = 4     # naranja

        elif pacientes[i]["síntomas"] == 'cefalea brusca' or pacientes[i]["síntomas"] == 'paresia' or pacientes[i]["síntomas"] == 'hipertension arterial' or pacientes[i]["síntomas"] == 'vertigo con afectacion vegetativa' or pacientes[i]["síntomas"] == 'sincope' or pacientes[i]["síntomas"] == 'urgencias psiquiatricas':
            pacientes[i]["gravedad"] = 3     # amarilla

        elif pacientes[i]["síntomas"] == 'otalgias' or pacientes[i]["síntomas"] == 'odontalgias' or pacientes[i]["síntomas"] == 'dolores inespecificos leves' or pacientes[i]["síntomas"] == 'traumatismos' or pacientes[i]["síntomas"] == 'esguinces' :
            pacientes[i]["gravedad"] = 2      # verde

        elif pacientes[i]["síntomas"] == 'cefalea' or pacientes[i]["síntomas"]== 'tos':
            pacientes[i]["gravedad"] = 1      # azul

        pacientes[i]["tiempo_espera"] = minutos_transcurridos()     # asigno el tiempo en el cual fue revisado


def cambiar_gravedad(pacientes):
    # chequear color y si su tiempo es mayor al tiempo de espera del siguiente cambiar color
    for i in range(len(pacientes)):
        if pacientes[i]["gravedad"] == 1 and pacientes[i]["tiempo_espera"] >= 120:  # llego al tiempo del verde -> lo cambio
            pacientes[i]["gravedad"] = 2

        if pacientes[i]["gravedad"] == 2 and pacientes[i]["tiempo_espera"] >= 60:  # llego al tiempo del amarillo -> lo cambio
            pacientes[i]["gravedad"] = 3

        if pacientes[i]["gravedad"] == 3 and pacientes[i]["tiempo_espera"] >= 50:  # llego al tiempo del naranja -> lo cambio
            pacientes[i]["gravedad"] = 4

        if pacientes[i]["gravedad"] == 4 and pacientes[i]["tiempo_espera"] >= 9:  # llego al tiempo del rojo -> lo cambio
            pacientes[i]["gravedad"] = 5


def atender_paciente(dni):
    pos = pacientes.index(pacientes["dni"])  # index busca la posicion en la lista
    del pacientes[pos]   # borra al paciente, se va del hospital


def dyc(pacientes):
    if len(pacientes) == 1:   # caso base 1: hay un solo paciente
        return pacientes

    if len(pacientes) == 2:   # caso base 2: hay dos pacientes. ordenamos y retornamos la lista ordenada
        if pacientes[0]["gravedad"] > pacientes[1]["gravedad"]:
          return pacientes
        else:
          pacientes_aux = pacientes[0]
          pacientes[0] = pacientes[1]
          pacientes[1] = pacientes_aux
          return pacientes


    else:
        medio = len(pacientes) // 2
        izq = dyc(pacientes[:medio])
        der = dyc(pacientes[medio:])
        pacientes = ordenamiento(izq, der)

    return pacientes      # ordenamos y devolvemos la lista de mayor a menor por merge sort


def ordenamiento(mitad1, mitad2):
    i, j = 0, 0
    lista_ordenada = []

    while i < len(mitad1) and j < len(mitad2):
        if mitad1[i]["gravedad"] > mitad2[j]["gravedad"]:
            lista_ordenada.append(mitad1[i])
            i += 1
        else:
            lista_ordenada.append(mitad2[j])
            j += 1

    # agregar lo que falta de una lista
    lista_ordenada += mitad1[i:]
    lista_ordenada += mitad2[j:]

    return lista_ordenada
