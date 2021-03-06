import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)
    
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
    
    def test_select_language(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
            
    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'reportes', report_name='hello-world-report'))