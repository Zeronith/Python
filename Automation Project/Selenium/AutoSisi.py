from selenium import webdriver
from selenium.webdriver.common.by import By
from pyautogui import screenshot
import time
import pyautogui
driver = webdriver.Chrome()


username = "23B1NUM0002"
password = "23b1num0002..."
driver.get("https://auth.num.edu.mn/oauth2/account/login?ReturnUrl=%2Foauth2%2Foauth%2Fauthorize%3Fclient_id%3Dae112b3cb474416b85c9be08538bba5c%26redirect_uri%3Dhttps%253A%252F%252Fauth.num.edu.mn%252Fapp%252Ftoken%26state%3D1PRTjg-s11YzENG1Dmi1vQ%26scope%3Dbio%2520notes%26response_type%3Dcode")
driver.implicitly_wait(10)
input_field = driver.find_element(By.CLASS_NAME , "form-control")
input_field.click()
input_field.send_keys(username)

pass_field = driver.find_element(By.ID, "password")
pass_field.click()
pass_field.send_keys(password)
login_button = driver.find_element(By.CLASS_NAME, "btn-block")
login_button.click()
sisi_button = driver.find_element(By.CLASS_NAME, "card-link")
sisi_button.click()
print("Current page title:", driver.title)
handles = driver.window_handles
driver.switch_to.window(handles[1])
print("Current page title:", driver.title)
time.sleep(5)
grade_button = driver.find_element(By.LINK_TEXT, "Дүнгийн мэдээлэл")
grade_button.click()
pyautogui.scroll(4)
time.sleep(15)
