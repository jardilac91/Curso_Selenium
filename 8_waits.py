import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_account_link(self):
        WebDriverWait(self.driver, 3).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')
        account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()


    def test_create_new_customer(self): #Creacion de nuevo usuario

        #Encontrar el elemento por el texto del enlace
        self.driver.find_element_by_link_text('ACCOUNT')

        #Hacer referencia a la cuenta
        my_account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'MY ACCOUNT')))
        my_account.click()

        #Referencia a crear una cuenta
        create_account = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account.click()

        #Verificacion de estado de pagina web
        WebDriverWait(self.driver, 3).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)