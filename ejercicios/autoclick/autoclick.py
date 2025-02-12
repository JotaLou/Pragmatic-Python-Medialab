
import pyautogui
import time

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
        time.sleep(1)
