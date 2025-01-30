from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytesseract
import pyautogui
from PIL import Image , ImageEnhance, ImageFilter

browser = webdriver.Chrome()
pyautogui.press("F11")
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

browser.implicitly_wait(3)
start_test=browser.find_element(By.CLASS_NAME, "gwt-Button")
start_test.click()
sleep(5)
screenshot = pyautogui.screenshot(region=(960,550,600,200))
screenshot.save("test.png")
image = Image.open("test.png")

# Apply a filter to reduce noise
last_test = pytesseract.image_to_string(image)
input_area = browser.find_element(By.CLASS_NAME, "challengeTextArea")
for text in last_test :
    input_area.send_keys(text)
input("Write quit if u want to close window")
