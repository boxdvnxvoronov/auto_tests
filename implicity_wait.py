from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")
try:

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:

    time.sleep(5)
    browser.quit()