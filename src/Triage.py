enfermeros: int
pacientes = []
medicos: int    # infinitos


def dyc(pacientes):
    if len(pacientes) == 0 or len(pacientes) == 1:  # caso base 1: esta vacia la lista o hay un solo paciente
        return pacientes

    if len(pacientes) == 2:   # caso base 2: hay dos pacientes, ordenamos y retornamos la lista ordenada
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