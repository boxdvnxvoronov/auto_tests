import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with open("/usr/share/dict/words", "r") as f:
    words = f.read().splitlines()

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

    for i, field in enumerate(elements):
        random_word = random.choice(words)
        field.send_keys(random_word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()