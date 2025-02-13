import tkinter as tk
import datetime

# Aplicación (Tkinter)
root = tk.Tk()
# Tiempo inicial
now = datetime.datetime.now()
texto_reloj = str(now.hour).zfill(2) +":"+str(now.minute).zfill(2)+":"+str(now.second).zfill(2) # Formato raro para que tenga leading zeroes

# Etiqueta de texto con el tiempo
time_label = tk.Label(root, text=texto_reloj) 
time_label.pack() # Mostrar etiqueta

# Funcion actualizar reloj
def actualizar_reloj():
    global time_label, now, texto_reloj
    now = datetime.datetime.now() # actualizamos tiempo
#   texto_reloj = f"{int(now.hour): 02d}:{int(now.minute): 02d}:{int(now.second): 02d}"
    texto_reloj = str(now.hour).zfill(2) +":"+str(now.minute).zfill(2)+":"+str(now.second).zfill(2)
    time_label.config(text=texto_reloj)
    
# ----------------- Bucle principal -------------------
if __name__ == '__main__':
    while True:
        root.update_idletasks()
        actualizar_reloj()
        print(texto_reloj)
        root.update()
# (Esta es una manera tosca de hacerlo)