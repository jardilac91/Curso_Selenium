import unittest
from selenium import webdriver

class Tables(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Sortable Data Tables").click()
    
    def test_sort_tables(self):
        driver = self.driver
        table = []
        
        sort = int(input("Por cual columna desea que se ordene la tabla \n 1 - Last Name \n 2 - First Name \n 3- Email \n 4 - Due \n"))


        for i in range(5):
            header = header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            if i == sort:
                header.click()
                break

        for i in range(4):
            data = {}
            for j in range(5):
                header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{j+1}]/span')
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{i+1}]/td[{j+1}]')
                #print(f"imprimo header {header.text}")
                #print(f"imprimo dato {row_data.text}")
                data.update({header.text:row_data.text})
            table.append(data)
        print(table)
    
    def tearDown(self):
        self.driver.implicitly_wait(20)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)