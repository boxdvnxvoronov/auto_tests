from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import unittest

class TestUT(unittest.TestCase):
    def test_UT1(self):
        link = "http://suninjuly.github.io/registration1.html"
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

    
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    
        welcome_text = welcome_text_elt.text

    
        self.assertEqual(welcome_text, welcome_text_elt.text, "Congratulations! You have successfully registered!")

    def test_UT2(self):
        link = "http://suninjuly.github.io/registration2.html"
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

    
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    
        welcome_text = welcome_text_elt.text
        
        self.assertEqual (welcome_text, welcome_text_elt.text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()