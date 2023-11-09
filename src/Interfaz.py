from src.Triage import atender_paciente, dyc
from datetime import datetime, timedelta
import tkinter as tk
import csv
import time

with open("DATOS.csv", "r") as tabla:
    csv_reader = csv.DictReader(tabla)  # lee por columnas
    # Passing the cav_reader object to list() to get a list of lists
    lista_pacientes = list(csv_reader)


INTERVALO_REFRESCO = 1
hora_inicio = datetime.now()
minutos_programa = 0
activo=False

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



def refrescar_tiempo_transcurrido():
    global activo
    if en_ejecucion:
        variable_hora_actual.set(obtener_tiempo_transcurrido_formateado())
        minutos_pasados_label.config(text=f"Minutos transcurridos: {minutos_transcurridos()}")
        raiz.after(INTERVALO_REFRESCO, refrescar_tiempo_transcurrido)
        reiniciar_cronometro()
        if minutos_transcurridos()>=10 and minutos_transcurridos() % 10 == 0 and activo==False:
            activo=True
            Hospital(lista_pacientes)
        if(minutos_transcurridos()% 5 == 0 and minutos_transcurridos()%2 != 0):
            activo= False


def rojos(pacientes):
    lista_aux=[]
    for i in range(len(pacientes)):
        if (pacientes[i]["gravedad"]== 5):
            lista_aux.append(pacientes[i]["nombre"])
    return lista_aux
def rojos(pacientes):
    lista_aux=[]
    for i in range(len(pacientes)):
        if (pacientes[i]["gravedad"]== 5):
            lista_aux.append(pacientes[i]["nombre"])
    return lista_aux
def naranjas(pacientes):
    lista_aux=[]
    for i in range(len(pacientes)):
        if (pacientes[i]["gravedad"]== 4):
            lista_aux.append(pacientes[i]["nombre"])
    return lista_aux
def amarillos(pacientes):
    lista_aux=[]
    for i in range(len(pacientes)):
        if (pacientes[i]["gravedad"]== 3):
            lista_aux.append(pacientes[i]["nombre"])
    return lista_aux
def verdes(pacientes):
    lista_aux=[]
    for i in range(len(pacientes)):
        if (pacientes[i]["gravedad"]== 2):
            lista_aux.append(pacientes[i]["nombre"])
    return lista_aux
def azules(pacientes):
    lista_aux=[]
    for i in range(len(pacientes)):
        if (pacientes[i]["gravedad"]== 1):
            lista_aux.append(pacientes[i]["nombre"])
    return lista_aux

 #todo:modificar para que elija la seleccion anterior si no seleccione una

def mostrar_lista_gravedad(seleccion):

    nueva_ventana = tk.Toplevel(raiz)
    nueva_ventana.title(f"Gravedad {seleccion}")
    lista_gravedad = tk.Listbox(nueva_ventana)
    lista_gravedad.pack()

    if seleccion == "rojos":
        elementos = rojos(lista_pacientes)
        lista_gravedad.config(font=("Arial", 18), fg="red")
    elif seleccion == "verdes":
        elementos = verdes(lista_pacientes)
        lista_gravedad.config(font=("Arial", 18), fg="green")
    elif seleccion == "azules":
        elementos = azules(lista_pacientes)
        lista_gravedad.config(font=("Arial", 18), fg="blue")
    elif seleccion == "amarillos":
        elementos = amarillos(lista_pacientes)
        lista_gravedad.config(font=("Arial", 18), fg="yellow")
    elif seleccion == "naranjas":
        elementos = naranjas(lista_pacientes)
        lista_gravedad.config(font=("Arial", 18), fg="orange")

    for elemento in elementos:
        lista_gravedad.insert(tk.END, elemento)

def asignar_enfermeros():
    if minutos_transcurridos() == 1380:  # minutos de 23 horas
        enfermeros = 1

    if minutos_transcurridos() == 360:  # minutos de 6 horas
        enfermeros = 2

    if minutos_transcurridos() == 600:  # minutos de 10 horas
        enfermeros = 5

    if minutos_transcurridos() == 960:  # minutos de 16 horas
        enfermeros = 3

    return enfermeros

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
    # chequear gravedad y si su tiempo es mayor al tiempo de espera del siguiente cambiar
    for i in range(len(pacientes)):
        if (minutos_transcurridos()-pacientes[i]["tiempo_espera"]) >= 120 and pacientes[i]["gravedad"] == 1 :  # llego al tiempo del verde -> lo cambio
            pacientes[i]["gravedad"] = 2
            pacientes[i]["tiempo_espera"]=minutos_transcurridos()

        if (minutos_transcurridos()-pacientes[i]["tiempo_espera"]) >= 60 and pacientes[i]["gravedad"] == 2:  # llego al tiempo del amarillo -> lo cambio
            pacientes[i]["gravedad"] = 3
            pacientes[i]["tiempo_espera"] = minutos_transcurridos()

        if  (minutos_transcurridos()-pacientes[i]["tiempo_espera"]) >= 50 and pacientes[i]["gravedad"] == 3:  # llego al tiempo del naranja -> lo cambio
            pacientes[i]["gravedad"] = 4
            pacientes[i]["tiempo_espera"] = minutos_transcurridos()

        if (minutos_transcurridos()-pacientes[i]["tiempo_espera"]) >= 9 and pacientes[i]["gravedad"] == 4 :  # llego al tiempo del rojo -> lo cambio
            pacientes[i]["gravedad"] = 5
            pacientes[i]["tiempo_espera"] = minutos_transcurridos()

    return pacientes
def Hospital(lista_pacientes):
    lista_pacientes = cambiar_gravedad(lista_pacientes)
    lista_ordenada=dyc(lista_pacientes)


raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value="00:00:00")
raiz.etiqueta = tk.Label(raiz, textvariable=variable_hora_actual, font="Consolas 60")
raiz.etiqueta.pack()

boton_iniciar = tk.Button(raiz, text="Iniciar Tiempo", command=iniciar_reloj, bg="green", fg="white")
boton_iniciar.pack(side="left")  # Coloca el botón a la izquierda

boton_detener = tk.Button(raiz, text="Detener Tiempo", command=detener_reloj, bg="red", fg="black")
boton_detener.pack(side="left")  # Coloca el botón a la izquierda

minutos_pasados_label = tk.Label(raiz, text="Minutos transcurridos: 0")
minutos_pasados_label.pack(side="left")

raiz.title("Menú Desplegable")

opciones = ["elija gravedad", "rojos", "naranjas", "amarillos","verdes","azules"]
seleccion = tk.StringVar(raiz)
seleccion.set(opciones[0])  # Valor predeterminado

menu_gravedad = tk.OptionMenu(raiz, seleccion, *opciones)
menu_gravedad.pack()

boton_mostrar_lista = tk.Button(raiz, text="despues de elegir gravedad, haga click aca", command=lambda: mostrar_lista_gravedad(seleccion.get()))

boton_mostrar_lista.pack()



app = tk.Frame()
raiz.title("reloj")

app.pack()
raiz.mainloop()


