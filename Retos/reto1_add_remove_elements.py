import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    
    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('cuantos elementos desea agregar?  '))
        elements_removed = int(input('Cuantos elementos deseas remover?  '))

        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for n in range(elements_added):
            add_button.click()
        
        for n in range(elements_removed):
            try:
                delete_button = driver.find_element_by_class_name("added-manually")
                delete_button.click()
            except:
                print("Esta intentando eliminar más botones de los que existen")
                break

        if total_elements > 0:
            print(f"Hay {total_elements} botones de eliminar en pantalla.")
        else:
            print("No hay botones de eliminar en pantalla")
        
        sleep(2)

    def tearDown(self):
	    self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
