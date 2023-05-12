import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    
    
    link = browser.find_element(By.LINK_TEXT, text)
    link.click()

    
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Bohdan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Voronov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Praha")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Czech Republic")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    
    time.sleep(2)
    
    browser.quit()

