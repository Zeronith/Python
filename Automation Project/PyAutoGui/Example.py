import pyautogui

s_width , s_height = pyautogui.size() # Return the size of primary monitor
print(s_width, s_height) # 2560 1600

current_mouse_x , current_mouse_y = pyautogui.position() # Return the current position of mouse 
print(current_mouse_x, current_mouse_y) # Of Course your output will be depends on your mouse position

pyautogui.moveTo(500,500) # Move the mouse to X Y coordinates

pyautogui.click() # Click the mouse
pyautogui.click(950,30) # Moves to given coordinate and click
#pyautogui.click("button.png") # Find where button.png appears on the screen and click it 


pyautogui.move(400,0) # Move the mouse 400 pixels to right of its current position 
#pyautogui.doubleClick() # Double click the mouse
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Moving mouse swiftly to given coordition over 2 second\

pyautogui.write("Hello world!", interval=0.25) # Type with pause with 0.25 sec in each key
pyautogui.press("esc") # Press Esc button
pyautogui.press("enter") # Press Enter button
pyautogui.moveTo(2000, 700)

with pyautogui.hold("shift") : # Press and hold (Shift Key)
    pyautogui.press('left') # Pressing left while holding shift

pyautogui.hotkey("ctrl", "c") # Press the Ctrl+C hotkey combination

pyautogui.alert("this is message to display") # Make alert box appear and pause program until Ok is clicked
