import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, "//*[@name='firstname']")
input1.send_keys('Bohdan')
input2 = browser.find_element(By.XPATH, "//*[@name='lastname']")
input2.send_keys('Voronov')
input2 = browser.find_element(By.XPATH, "//*[@name='email']")
input2.send_keys('bohdanvoronov@pythonmail.com')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.XPATH, "//*[@id='file']")
element.send_keys(file_path)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(2)

browser.quit()