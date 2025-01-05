# Explicit Wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'class_name'), # Element filtration
        "Text_You_Are_Expecting"# Expected text
    )
)
# Much More Custom , Use that we need to wait until some condition fulfilled
