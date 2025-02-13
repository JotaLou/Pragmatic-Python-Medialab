'''
    Ejemplo de reloj
'''
from time import sleep
import datetime as dt

# Tiempo inicial
now = dt.datetime.now()
texto_reloj = str(now.hour).zfill(2) +":"+str(now.minute).zfill(2)+":"+str(now.second).zfill(2) # Formato raro para que tenga leading zeroes

# Funcion actualizar reloj
def actualizar_reloj():
    global now, texto_reloj
    now = dt.datetime.now() # actualizamos tiempo
#   texto_reloj = f"{int(now.hour): 02d}:{int(now.minute): 02d}:{int(now.second): 02d}"
    texto_reloj = str(now.hour).zfill(2) +":"+str(now.minute).zfill(2)+":"+str(now.second).zfill(2)

while True:
    actualizar_reloj()
    print(texto_reloj)
    sleep(1)
