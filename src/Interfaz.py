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

def mostrar_lista_color(seleccion):
    nueva_ventana = tk.Toplevel(raiz)
    nueva_ventana.title(f"Elementos de color {seleccion}")

    lista_color = tk.Listbox(nueva_ventana)
    lista_color.pack()

    if seleccion == "rojos":
        elementos = ["Manzana", "Fresa", "Cereza", "Tomate"] #todo: modificar esto por el csv
    elif seleccion == "verdes":
        elementos = ["Manzana", "Uva", "Pepino", "Pimiento"]
    elif seleccion == "azules":
        elementos = ["Cielo", "Mar", "Zafiro", "Arándano"]
    elif seleccion == "amarillos":
        elementos = ["Plátano", "Limón", "Maíz", "Girasol"]
    elif seleccion == "naranjas":
        elementos = ["Naranja", "Mandarina", "Zanahoria", "Calabaza"]

    for elemento in elementos:
        lista_color.insert(tk.END, elemento)

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

opciones = ["elija gravedad", "rojos", "verdes", "azules", "amarillos", "naranjas"]
seleccion = tk.StringVar(raiz)
seleccion.set(opciones[0])  # Valor predeterminado

menu_color = tk.OptionMenu(raiz, seleccion, *opciones)
menu_color.pack()

boton_mostrar_lista = tk.Button(raiz, text="Mostrar Lista", command=lambda: mostrar_lista_color(seleccion.get()))
boton_mostrar_lista.pack()



app = tk.Frame()
raiz.title("reloj")


app.pack()
raiz.mainloop()