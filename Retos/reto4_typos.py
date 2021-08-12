import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Typos").click()
    
    def test_find_typo(self):
        driver = self.driver

        tries = 0
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while not found:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            print(text_to_check)
            if text_to_check == correct_text:
                tries += 1
                found = True
            else:
                tries += 1
                driver.refresh()

        print(f"Tomó {tries} intentos encontrar la frase correcta")

    def tearDown(self):
	    self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)