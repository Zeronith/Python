import pyautogui

# General Function

pyautogui.position() # Returns the position of mouse (x, y)
pyautogui.size() # Returns the size of primary monitor (x, y)
pyautogui.onScreen(x, y) # True if x and y are within the screen

# Mouse Function

pyautogui.moveTo(x, y, duration=num_seconds) # Move mouse to X Y coordinates over num_second seconds
pyautogui.moveRel(x, y, duration=num_seconds) # Move mouse relative to its current mouse position

# IF DURATION IS 0 OR UNSPECIFIED , MOVEMENT IS IMMEDIATE


pyautogui.dragTo(x, y,duration=num_seconds ) # Drag mouse to X Y 
pyautogui.dragRel(x, y, duration=num_seconds)  # Drag mouse relative to current position of mouse


pyautogui.click(x = MoveToX , y = MoveToY, clicks=Number_Of_Clicks, interval=secs_between_clicks, button="left")



pyautogui.mouseDown(x=MoveToX, y=MoveToY, button='left')
pyautogui.mouseUp(x=MoveToX, y=MoveToY, button='left')


# Keyboard Function

pyautogui.typewrite("Hello World!\n", interval=secs_between_keys) # Useful for entering text , \n is Enter
pyautogui.typewrite(["a", "b","c"]) # List of keys can be passed too

# If you have image file of something you want to click on 
pyautogui.locateOnScreen("lookslikethis.png") # Returns (left , top, width , height) of first place it is found
pyautogui.locateAllOnScreen() # Returns all location that found as list

pyautogui.onScreen(0,0) # True
pyautogui.onScreen(1000,0) # Fakse
pyautogui.onScreen(300,300) # True

# There is two different way to write text

# Typewrite is like human typing writing like human char by char also this one comes with interval
# Write is like writing in string , also this one doesnt have interval


# Typewriter for human-like writing
# Write is for faster and simpler