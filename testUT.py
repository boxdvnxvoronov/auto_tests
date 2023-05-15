from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import unittest

def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group first_class']//input")
    input1.send_keys("BOHDAN")
    input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group second_class']//input")
    input2.send_keys("VORONOV")
    input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group third_class']//input")
    input3.send_keys("bohdvnvoronov@kosmomail.com")

    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

   
    time.sleep(1)

class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
      self.assertEqual(fill_form("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "registration is failed")

if __name__ == "__main__":
    unittest.main()

