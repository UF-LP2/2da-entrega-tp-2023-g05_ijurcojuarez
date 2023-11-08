from Cronometro import obtener_tiempo_transcurrido_formateado

enfermeros: int
pacientes = [ ]
medicos: int    #infinitos

def AsignarEnfermeros():
    if obtener_tiempo_transcurrido_formateado() == 23:
        enfermeros = 1

    if obtener_tiempo_transcurrido_formateado() == 6:
        enfermeros = 2

    if obtener_tiempo_transcurrido_formateado() == 10:
        enfermeros = 5

    if obtener_tiempo_transcurrido_formateado() == 16:
        enfermeros = 3


def AsignarGravedad(pacientes):
    for i in range(len(pacientes)):
        if pacientes[i].síntomas == 'politraumatismo grave':
            pacientes.gravedad= 5    # rojo

        elif pacientes[i].síntomas  == 'coma' or pacientes[i].síntomas== 'convulsiones' or pacientes[i].síntomas == 'hemorragia digestiva' or pacientes[i].síntomas == 'isquemia':
            pacientes[i].gravedad= 4     #naranja

        elif pacientes[i].síntomas == 'cefalea brusca' or pacientes[i].síntomas == 'paresia' or pacientes[i].síntomas == 'hipertension arterial' or pacientes[i].síntomas == 'vertigo con afectacion vegetativa'or pacientes[i].síntomas == 'sincope'or pacientes[i].síntomas == 'urgencias psiquiatricas':
            pacientes[i].gravedad = 3     #amarilla


        elif pacientes[i].síntomas == 'otalgias' or pacientes[i].síntomas == 'odontalgias' or pacientes[i].síntomas == 'dolores inespecificos leves' or pacientes[i].síntomas == 'traumatismos'or pacientes[i].síntomas == 'esguinces':
            pacientes[i].gravedad= 2      #verde


        elif pacientes[i].síntomas == 'cefalea' or pacientes[i].síntomas == 'tos':
            pacientes[i].gravedad= 1      #azul

        pacientes[i].tiempo_espera = obtener_tiempo_transcurrido_formateado()     #asigno el tiempo en el cual fue revisado



def CambiarGravedad(pacientes):
    for i in range(len(pacientes)):
      if obtener_tiempo_transcurrido_formateado()  > pacientes[i].tiempo_espera:
        pacientes[i].gravedad= 5 #cuando ya pasó su tiempo se lo atiende inmediatamente


def AtenderPaciente(dni):
    pos=pacientes.index(pacientes.dni)  #index busca la posicion en la lista
    del pacientes[pos]   #borra al paciente, se va del hospital


def DyC(pacientes):
    if len(pacientes) == 1:   #caso base 1: hay un solo paciente
        return pacientes

    if len(pacientes) == 2:   #caso base 2: hay dos pacientes. ordenamos y retornamos la lista ordenada
        if (pacientes.gravedad[0] > pacientes.gravedad[1]):
          return pacientes
        else:
          pacientes_aux= pacientes[0]
          pacientes[0]=pacientes[1]
          pacientes[1]=pacientes_aux
          return pacientes


    else:
        medio = len(pacientes) // 2
        izq = DyC(pacientes[:medio])
        der = DyC(pacientes[medio:])
        pacientes = Ordenamiento(izq, der)

    return pacientes      # ordenamos y devolvemos la lista de mayor a menor por merge sort


def Ordenamiento(mitad1, mitad2):
    i, j = 0, 0
    lista_ordenada = []

    while (i < len(mitad1) and j < len(mitad2)):
        if (mitad1.gravedad[i] > mitad2.gravedad[j]):
            lista_ordenada.append(mitad1[i])
            i += 1
        else:
            lista_ordenada.append(mitad2[j])
            j += 1

    # Agregar lo que falta de una lista
    lista_ordenada += mitad1[i:]
    lista_ordenada += mitad2[j:]

    return lista_ordenada
