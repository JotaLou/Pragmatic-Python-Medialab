''' Ejercicio del cursillo pragmatic python impartido en MediaLab
    Enunciado: Hacer una aplicación de reloj digital. (Empezar con terminal)
'''
import tkinter as tk
''' Importar los módulos pertinentes, eliminar este comentario'''

# Aplicación (Tkinter)
root = tk.Tk()
# Obtener el tiempo
'''
    Rellenar con código, eliminar este comentario
'''
texto_reloj="" #Rellenar esta variable con el texto del reloj "hh:mm:ss"

# Etiqueta de texto con el tiempo
time_label = tk.Label(root, text=texto_reloj) 
time_label.pack() # Mostrar etiqueta

# Funcion actualizar reloj
def actualizar_reloj():
    global time_label, texto_reloj
'''
    Rellenar con código, eliminar este comentario
'''




# ----------------- Bucle principal -------------------
if __name__ == '__main__':
    while True:
        root.update_idletasks()
        actualizar_reloj()
        print(texto_reloj)
        root.update()
# (Esta es una manera tosca de hacerlo)