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
pyautogui.doubleClick() # Double click the mouse
pyautogui.move(500, 500, duration=2, tween=pyautogui.easeInOutQuad)