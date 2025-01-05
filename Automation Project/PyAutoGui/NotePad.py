import pyautogui
import time

# Hold down the Win key and press "S" to open the search bar
pyautogui.keyDown("win")  # Hold down the Win key
pyautogui.press("s")      # Press the "S" key
pyautogui.keyUp("win")    # Release the Win key
time.sleep(3)
pyautogui.write("Notepad")
pyautogui.press("Enter")
time.sleep(3)

pyautogui.typewrite("Hello. My name is Enguunbayr. Surprise", interval=0.1)
