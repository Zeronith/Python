from selenium import webdriver # Importing for gaining access to various browser automation function
from selenium.webdriver.common.by import By # Importing for making it easier to search "By" class and id and name etc
from time import sleep # Importing this for making it not instanious close
number = "88999419" # Saving my email
driver = webdriver.Chrome() # Making driver as chrome driver and make it easier to use automation function of chrome 
driver.get("https://www.facebook.com/") # Going to given URL
driver.implicitly_wait(4) # if screen is loading it will wait given time , if its loads faster its automatically continue to execute next line 
email=driver.find_element(By.ID, "email") # Finding email input by By and assigning it into email variable
email.click() # Clicking into email input part by clicking on it
email.send_keys(number) # Entering the login info by variable's i have provided
password = "aYANAKOJIKIYOTAKA0730..." # Saving my password
passw=driver.find_element(By.ID , "pass") # Finding password input by By and assigning it into passw variable
passw.click() # Clicking to password input part by clicking on it
passw.send_keys(password) # Entering the login info by variable's i have provided
Log_button=driver.find_element(By.NAME, "login") # Searching for Login button by name
Log_button.click() # Clicking on it to Login
sleep(10) # Waits 10 sec
driver.quit() # Closes browser
