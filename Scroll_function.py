import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 200);")
input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
input1.send_keys(y)
option1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
option1.click()
option1 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
option1.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(2)

browser.quit()
