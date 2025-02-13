''' Ejercicio del cursillo pragmatic python impartido en MediaLab
    Enunciado: Hacer una gráfica de la función: sen(2πf), f∈[0,20000]; step de 1
'''
import math
from matplotlib import pyplot as plt

USE_NUMPY = False
SIZE = 1000
if(USE_NUMPY == True):
    # Version numpy
    import numpy as np
    x = np.linspace(0, 2*math.pi, SIZE) # Creamos los elementos de x
else:
    # Version sin numpy
    temp = range(0, SIZE, 1)
    x = [(2*math.pi*value)/SIZE for value in temp] # List Comprehension
        
y = []   # Inicializamos y como una lista vacía
for value in x:  #Añadimos uno a uno valores a y
    y.append(math.sin(2*math.pi*value)) 
# Preparamos el gráfico
plt.plot(x,y)
plt.xlabel("x")      # Etiqueta x
plt.ylabel("sen(x)") # Etiqueta y
# Lo mostramos en pantalla
plt.show()