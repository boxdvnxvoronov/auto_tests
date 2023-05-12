from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    
    input1 = browser.find_element(By.XPATH, "//*[@name='first_name']")
    input1.send_keys("Bohdan")
    input2 = browser.find_element(By.XPATH, "//*[@name='last_name']")
    input2.send_keys("Voronov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Praha")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Czech Republic")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    
    time.sleep(2)
    
    browser.quit()