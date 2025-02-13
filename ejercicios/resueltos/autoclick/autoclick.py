''' Ejercicio del cursillo pragmatic python impartido en MediaLab
    Enunciado: Hacer un script que pulse un botón en pantalla cada segundo.
'''
import pyautogui
from time import sleep

filename = "Download"
extension = ".png"

while True:
    print("Trying to click")
    try:
        location = pyautogui.locateOnScreen(filename + extension)
        pyautogui.click(location)
    except:
        print("Image not found.")
    else:
        pyautogui.moveTo(100, 200)
    finally:
        print("Waiting 1 second...")
        sleep(1)
