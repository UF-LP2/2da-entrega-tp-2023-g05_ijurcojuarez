from Interfaz import minutos_transcurridos

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
        if pacientes[i]["sintomas"] == 'politraumatismo grave':
            pacientes[i]["gravedad"] = 5  # rojo

        elif pacientes[i]["sintomas"] == 'coma' or pacientes[i]["sintomas"] == 'convulsiones' or pacientes[i]["sintomas"] == 'hemorragia digestiva' or pacientes[i]["sintomas"] == 'isquemia':
            pacientes[i]["gravedad"] = 4  # naranja

        elif pacientes[i]["sintomas"] == 'cefalea brusca' or pacientes[i]["sintomas"] == 'paresia' or pacientes[i]["sintomas"] == 'hipertension arterial' or pacientes[i]["sintomas"] == 'vertigo con afectacion vegetativa' or pacientes[i]["sintomas"] == 'sincope' or pacientes[i]["sintomas"] == 'urgencias psiquiatricas':
            pacientes[i]["gravedad"] = 3  # amarilla

        elif pacientes[i]["sintomas"] == 'otalgias' or pacientes[i]["sintomas"] == 'odontalgias' or pacientes[i]["sintomas"] == 'dolores inespecificos leves' or pacientes[i]["sintomas"] == 'traumatismos' or pacientes[i]["sintomas"] == 'esguinces':
            pacientes[i]["gravedad"] = 2  # verde

        elif pacientes[i]["sintomas"] == 'cefalea' or pacientes[i]["sintomas"] == 'tos':
            pacientes[i]["gravedad"] = 1  # azul

        pacientes[i]["tiempo_espera"] = minutos_transcurridos()  # asigno el tiempo en el cual fue revisado


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
    pos = pacientes.index(dni)  # index busca la posicion en la lista
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
