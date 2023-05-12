import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.XPATH, "//*[@type='submit']")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
input1.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(7)

browser.quit()