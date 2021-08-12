import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/disappearing_elements')
    
    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options)<5:
            options.clear()

            for n in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{n + 1}]/a')
                    options.append(option_name.text)
                except:
                    print(f"Option number {n+1} is Not Found")
                    tries += 1
                    driver.refresh()

        print(f"Finalizó en {tries} intentos")


    def tearDown(self):
	    self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
