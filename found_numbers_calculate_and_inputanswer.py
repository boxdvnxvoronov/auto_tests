import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(num1, num2):
    return str(int(num1)+int(num2))


a = int(browser.find_element(By.XPATH, "//*[@id='num1']").text)
b = int(browser.find_element(By.XPATH, "//*[@id='num2']").text)
c = calc(a, b)

select = Select(browser.find_element(By.XPATH, "//*[@id='dropdown']"))
select.select_by_value(c)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(2)

browser.quit()