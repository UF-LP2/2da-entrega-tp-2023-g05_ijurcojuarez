from datetime import datetime, timedelta
import tkinter as tk
import csv


INTERVALO_REFRESCO = 1
hora_inicio = datetime.now()
minutos_programa = 0

with open("DATOS.csv", "r") as tabla:
    csv_reader = csv.DictReader(tabla)  # lee por columnas
    # Passing the cav_reader object to list() to get a list of lists
    pacientes = list(csv_reader)
def iniciar_reloj():
    global hora_inicio, en_ejecucion
    hora_inicio = datetime.now()
    en_ejecucion = True
    refrescar_tiempo_transcurrido()


def detener_reloj():
    global en_ejecucion
    en_ejecucion = False

def rojos():
    lista_aux= []
    for i in range(len(pacientes)):
        if pacientes[i]["gravedad"] == 5:
            lista_aux.append(pacientes[i])
    print(lista_aux) #todo: ver como se imprime la lista!!

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
    if minutos_transcurridos() == 1380:
        global hora_inicio, en_ejecucion
        hora_inicio = datetime.now()
        en_ejecucion = True



def refrescar_tiempo_transcurrido():
    if en_ejecucion:
        variable_hora_actual.set(obtener_tiempo_transcurrido_formateado())
        minutos_pasados_label.config(text=f"Minutos transcurridos: {minutos_transcurridos()}")
        raiz.after(INTERVALO_REFRESCO, refrescar_tiempo_transcurrido)
        reiniciar_cronometro()

def mostrar_lista(opcion):
    nueva_ventana = tk.Toplevel(raiz)
    nueva_ventana.title(f"Lista de {opcion}")

    # Lista de elementos pre-cargados
    elementos = []

    if opcion == "Nombres":
        elementos = pacientes
    elif opcion == "Colores":
        elementos = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja"]

    lista = tk.Listbox(nueva_ventana)
    lista.pack()

    for elemento in elementos:
        lista.insert(tk.END, elemento)


raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value="00:00:00")
raiz.etiqueta = tk.Label(raiz, textvariable=variable_hora_actual, font="Consolas 60")
raiz.etiqueta.pack(side="top")


raiz.title("Menú Desplegable")

opciones = ["Nombres", "Colores"]

opcion_var = tk.StringVar()
opcion_var.set(opciones[0])

menu_desplegable = tk.OptionMenu(raiz, opcion_var, *opciones)
menu_desplegable.pack()

boton_mostrar = tk.Button(raiz, text="Mostrar Lista", command=lambda: mostrar_lista(opcion_var.get()))
boton_mostrar.pack()
boton_iniciar = tk.Button(raiz, text="Iniciar", command=iniciar_reloj)
boton_iniciar.pack()

boton_detener = tk.Button(raiz, text="Detener", command=detener_reloj)
boton_detener.pack()

boton_rojo = tk.Button(raiz, text="rojos", command=rojos, bg="red")
rojos_label = tk.Label(raiz, text="rojos: ")
boton_rojo.pack(side="top")

minutos_pasados_label = tk.Label(raiz, text="Minutos transcurridos: 0")
minutos_pasados_label.pack()

app = tk.Frame()
raiz.title("reloj")


app.pack()
raiz.mainloop()