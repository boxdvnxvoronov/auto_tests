from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:

    button = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)

    button = browser.find_element(By.XPATH, "//*[@id='solve']")
    button.click()

finally:
    time.sleep(7)
    browser.quit