from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
browser = webdriver.Chrome()
browser.get("https://play.typeracer.com/")
sleep(5)
browser.find_element(By.LINK_TEXT, "Enter a Typing Race").click()
sleep(10)
spans=browser.find_elements(By.XPATH, "//span[@unselectable]")
full_text = spans[0].text + spans[1].text + " " +spans[2].text
input_field = browser.find_element(By.CLASS_NAME, "txtInput")
sleep(5)
for text in full_text :
    input_field.send_keys(text) # If u want to make it faster , just import pyautogui.typewrite. (Its better since u can configure interval between character)
    print(text)
input("Write quit if u want to close window")
