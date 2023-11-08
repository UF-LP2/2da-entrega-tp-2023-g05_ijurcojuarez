from datetime import datetime
import tkinter as tk
INTERVALO_REFRESCO = 1000  # En milisegundos

#hora_inicio = datetime.now()
segundos_transcurridos=-2

def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 15 / 5)
    segundos -= horas * 15 * 5
    minutos = int(segundos / 5)
    segundos -= minutos * 5
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"



def reiniciar_cronometro():
    global segundos_transcurridos
    segundos_transcurridos = 0

def obtener_tiempo_transcurrido_formateado():
    global segundos_transcurridos
    segundos_transcurridos += 1
    if segundos_transcurridos == 24:  # Si han pasado 23 horas
        reiniciar_cronometro()
    return segundos_a_segundos_minutos_y_horas(segundos_transcurridos)


def refrescar_tiempo_transcurrido():
    #print("Refrescando!")
    variable_hora_actual.set(obtener_tiempo_transcurrido_formateado())
    raiz.after(INTERVALO_REFRESCO, refrescar_tiempo_transcurrido)


raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value=obtener_tiempo_transcurrido_formateado())
raiz.etiqueta = tk.Label(
    raiz, textvariable=variable_hora_actual, font=f"Consolas 60")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("Cronómetro con Tkinter - By Parzibyte")
refrescar_tiempo_transcurrido()
app.pack()
app.mainloop()