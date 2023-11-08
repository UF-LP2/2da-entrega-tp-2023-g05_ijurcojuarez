from datetime import datetime
import tkinter as tk

INTERVALO_REFRESCO = 1000  # En milisegundos (1 segundo real)

hora_inicio = datetime.now()
minutos_programa = 0

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

def refrescar_tiempo_transcurrido():
    if en_ejecucion:
        variable_hora_actual.set(obtener_tiempo_transcurrido_formateado())
        minutos_pasados_label.config(text=f"Minutos transcurridos: {minutos_transcurridos()}")
        raiz.after(INTERVALO_REFRESCO, refrescar_tiempo_transcurrido)

raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value="00:00:00")
raiz.etiqueta = tk.Label(raiz, textvariable=variable_hora_actual, font="Consolas 60")
raiz.etiqueta.pack(side="top")

boton_iniciar = tk.Button(raiz, text="Iniciar", command=iniciar_reloj)
boton_iniciar.pack()

boton_detener = tk.Button(raiz, text="Detener", command=detener_reloj)
boton_detener.pack()

minutos_pasados_label = tk.Label(raiz, text="Minutos transcurridos: 0")
minutos_pasados_label.pack()

app = tk.Frame()
raiz.title("reloj")

app.pack()
raiz.mainloop()