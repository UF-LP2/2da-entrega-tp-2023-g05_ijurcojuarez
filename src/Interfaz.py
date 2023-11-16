from src.Triage import dyc
from datetime import datetime
import tkinter as tk
import csv

with open("DATOS.csv", "r") as tabla:
    csv_reader = csv.DictReader(tabla)  # lee por columnas
    # Passing the cav_reader object to list() to get a list of lists
    personas = list(csv_reader)

lista_pacientes = []
INTERVALO_REFRESCO = 1000
en_ejecucion = False
hora_inicio = datetime.now()
minutos_programa = 0
activo = False
#nueva_ventana = None


# lista_gravedad = "SELECCIONE GRAVEDAD"


def iniciar_reloj():
    global hora_inicio, en_ejecucion
    hora_inicio = datetime.now()
    en_ejecucion = True
    refrescar_tiempo_transcurrido()
    asignar_gravedad(lista_pacientes)
    print(lista_pacientes)
    dyc(lista_pacientes)


def detener_reloj():
    global en_ejecucion
    en_ejecucion = False


def minutos_transcurridos():
    segundos_transcurridos = (datetime.now() - hora_inicio).total_seconds()
    minutos_programa = int(segundos_transcurridos)
    return minutos_programa


def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas * 60 * 60
    minutos = int(segundos / 60)
    segundos -= minutos * 60
    return f"{horas:02d}:{minutos:02d}:{int(segundos):02d}"


def obtener_tiempo_transcurrido_formateado():
    global minutos_programa
    if en_ejecucion:
        segundos_reales = (datetime.now() - hora_inicio).total_seconds()
        minutos_programa = int(segundos_reales)  # Cada minuto en el programa avanza a medida que pasa 1 segundo real
    horas_programa = minutos_programa / 60
    return segundos_a_segundos_minutos_y_horas(int(horas_programa * 60 * 60))


def reiniciar_cronometro():
    if minutos_transcurridos() == 1439:
        global hora_inicio, en_ejecucion
        hora_inicio = datetime.now()
        en_ejecucion = True


def asignar_enfermeros():
    enfermeros = 2
    if minutos_transcurridos() == 1380:  # minutos de 23 horas
        enfermeros = 1

    if minutos_transcurridos() == 360:  # minutos de 6 horas
        enfermeros = 2

    if minutos_transcurridos() == 600:  # minutos de 10 horas
        enfermeros = 5

    if minutos_transcurridos() == 960:  # minutos de 16 horas
        enfermeros = 3

    if minutos_transcurridos() % 5 == 0 and minutos_transcurridos() >= 5 and len(
            personas) != 0:  # cada 5 mins atiende un paciente
        llamar_pacientes(enfermeros)


def llamar_pacientes(enfermeros):
    enfermeria = []
    if len(personas) >= enfermeros:
        for i in range(enfermeros):
            enfermeria.append(personas[i])
            # print(enfermeria)
            del personas[i]
            asignar_gravedad(enfermeria)
    else:
        for i in range(len(personas)):
            enfermeria.append(personas[i])
            del personas[i]
            asignar_gravedad(enfermeria)


def refrescar_tiempo_transcurrido():
    global activo
    if en_ejecucion:
        variable_hora_actual.set(obtener_tiempo_transcurrido_formateado())
        # minutos_pasados_label.config(text=f"Minutos transcurridos: {minutos_transcurridos()}")
        raiz.after(INTERVALO_REFRESCO, refrescar_tiempo_transcurrido)
        reiniciar_cronometro()
        asignar_enfermeros()
        # mostrar_lista_gravedad()
        if minutos_transcurridos() >= 10 and minutos_transcurridos() % 10 == 0 and activo == False:
            activo = True
            hospital(lista_pacientes)
        if minutos_transcurridos() % 5 == 0 and minutos_transcurridos() % 2 != 0:
            activo = False
        if minutos_transcurridos() % 5 == 0 and minutos_transcurridos() >= 5:  # cada 5 mins atiende un paciente
            atender_paciente()


def atender_paciente():
    del lista_pacientes[0]  # borra al paciente, se va del hospital


def color(pacientes, gravedad):
    lista_aux = []
    for i in range(len(pacientes)):
        if pacientes[i]["gravedad"] == gravedad:
            lista_aux.append(pacientes[i]["apellido"] + "," + pacientes[i]["dni"])
    return lista_aux


def mostrar_lista_gravedad(seleccion):
    nueva_ventana = tk.Toplevel(raiz)
    nueva_ventana.title(f"Gravedad {seleccion}")
    lista_gravedad = tk.Listbox(nueva_ventana)
    lista_gravedad.pack()

    if seleccion == "elija gravedad":
        elementos = ["ELIJA GRAVEDAD!!!"]
        lista_gravedad.config(font=(")Arial", 18))
    elif seleccion == "rojos":
        elementos = color(lista_pacientes ,5)
        lista_gravedad.config(font=("Arial", 18), fg="red")
    elif seleccion == "verdes":
        elementos = color(lista_pacientes, 2)
        lista_gravedad.config(font=("Arial", 18), fg="green")
    elif seleccion == "azules":
        elementos = color(lista_pacientes,1)
        lista_gravedad.config(font=("Arial", 18), fg="blue")
    elif seleccion == "amarillos":
        elementos = color(lista_pacientes, 3)
        lista_gravedad.config(font=("Arial", 18), fg="yellow")
    elif seleccion == "naranjas":
        elementos = color(lista_pacientes, 4)
        lista_gravedad.config(font=("Arial", 18), fg="orange")

    for elemento in elementos:
        lista_gravedad.delete(0, tk.END)  # borra lo q hay en la lista
        lista_gravedad.insert(tk.END, elemento)


"""
    def crear_ventana():
        global nueva_ventana
        if nueva_ventana == None:
            nueva_ventana = tk.Toplevel(raiz)

        return
"""


def asignar_gravedad(pacientes):
    for i in range(len(pacientes) -1, -1, -1):

        if pacientes[i]["sintomas"] == 'politraumatismo grave':
            pacientes[i]["gravedad"] = 5  # rojo

        elif pacientes[i]["sintomas"] == 'coma' or pacientes[i]["sintomas"] == 'convulsiones' or pacientes[i][
            "sintomas"] == 'hemorragia digestiva' or pacientes[i]["sintomas"] == 'isquemia':
            pacientes[i]["gravedad"] = 4  # naranja

        elif pacientes[i]["sintomas"] == 'cefalea brusca' or pacientes[i]["sintomas"] == 'paresia' or pacientes[i][
            "sintomas"] == 'hipertension arterial' or pacientes[i]["sintomas"] == 'vertigo con afectacion vegetativa' or \
                pacientes[i]["sintomas"] == 'sincope' or pacientes[i]["sintomas"] == 'urgencias psiquiatricas':
            pacientes[i]["gravedad"] = 3  # amarilla

        elif pacientes[i]["sintomas"] == 'otalgias' or pacientes[i]["sintomas"] == 'odontalgias' or pacientes[i][
            "sintomas"] == 'dolores inespecificos leves' or pacientes[i]["sintomas"] == 'traumatismos' or pacientes[i][
            "sintomas"] == 'esguinces':
            pacientes[i]["gravedad"] = 2  # verde

        elif pacientes[i]["sintomas"] == 'cefalea' or pacientes[i]["sintomas"] == 'tos':
            pacientes[i]["gravedad"] = 1  # azul
        else:
            del pacientes[i]  # elimina el paciente si tiene basura en el sintoma
        pacientes[i]["tiempo_espera"] = minutos_transcurridos()  # asigno el tiempo en el cual fue revisado
        lista_pacientes.append(pacientes[i])
        print(lista_pacientes)


def cambiar_gravedad(pacientes):
    tiempo_actual = minutos_transcurridos()

    for i in range(len(pacientes)):
        tiempo_transcurrido = tiempo_actual - pacientes[i]["tiempo_espera"]

        if tiempo_transcurrido >= 120 and pacientes[i]["gravedad"] == 1:
            pacientes[i]["gravedad"] = 2
            pacientes[i]["tiempo_espera"] = tiempo_actual

        elif tiempo_transcurrido >= 60 and pacientes[i]["gravedad"] == 2:
            pacientes[i]["gravedad"] = 3
            pacientes[i]["tiempo_espera"] = tiempo_actual

        elif tiempo_transcurrido >= 50 and pacientes[i]["gravedad"] == 3:
            pacientes[i]["gravedad"] = 4
            pacientes[i]["tiempo_espera"] = tiempo_actual

        elif tiempo_transcurrido >= 9 and pacientes[i]["gravedad"] == 4:
            pacientes[i]["gravedad"] = 5
            pacientes[i]["tiempo_espera"] = tiempo_actual

    return pacientes


def hospital(lista_pacientes):
    lista_pacientes = cambiar_gravedad(lista_pacientes)
    lista_pacientes = dyc(lista_pacientes)


raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value="00:00:00")
raiz.etiqueta = tk.Label(raiz, textvariable=variable_hora_actual, font="Consolas 60")
raiz.etiqueta.pack()

boton_iniciar = tk.Button(raiz, text="Reiniciar Tiempo", command=iniciar_reloj, bg="green", fg="white")
boton_iniciar.pack(side="left")  # Coloca el botón a la izquierda

boton_detener = tk.Button(raiz, text="Detener Tiempo", command=detener_reloj, bg="red", fg="black")
boton_detener.pack(side="left")  # Coloca el botón a la izquierda

# minutos_pasados_label = tk.Label(raiz, text="Minutos transcurridos: 0")
# minutos_pasados_label.pack(side="left")

raiz.title("Menú Desplegable")

opciones = ["elija gravedad", "rojos", "naranjas", "amarillos", "verdes", "azules"]
seleccion = tk.StringVar(raiz)
seleccion.set(opciones[0])  # Valor predeterminado

menu_gravedad = tk.OptionMenu(raiz, seleccion, *opciones)
menu_gravedad.pack()

boton_mostrar_lista = tk.Button(raiz, text="despues de elegir gravedad, haga click aca",
                                command=lambda: mostrar_lista_gravedad(seleccion.get()))
boton_mostrar_lista.pack()

app = tk.Frame()
raiz.title("reloj")

app.pack()