# IMPLICIT WAIT
from selenium import webdriver 
driver = webdriver.Chrome()
driver.implicitly_wait(10) # Wait up to 10 seconds for elements to appear

driver.get("asurascans.com")
element = driver.find_element("id", "example-id") # Uses implicit wait 
# If element found in 10 sec its going to continue
driver.quit()

# Implicit wait is applied to whole code


# EXPLICIT WAIT
'''
Waits for a specific condition to be met for particular element or scenerio before proceeding .
You define the condition and the maximum wait time
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://example.com")
try :
    # Wait up to 10 seconds for the element to be clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(By.Id, "example-id")
    )
    element.click()
finally :
    driver.quit()
'''

Feature	    Implicit Wait	                Explicit Wait
Scope	    All elements in the session.	Specific element or condition.
Condition	Presence in DOM.	            Flexible (e.g., visibility, clickability).
Usage	    Simple to set up.	            Requires more detailed implementation.
Efficiency	May lead to unnecessary waits.	More precise and efficient.
'''