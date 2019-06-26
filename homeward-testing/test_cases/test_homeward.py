import sys
sys.path.append('../pages')
import unittest
import time
from selenium import webdriver
from login import Login
from situation_page import Situation

class Homeward_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://homeward-crm-stage.herokuapp.com/applications')
        self.driver.implicitly_wait(10)

    def test_homeward(self):
        login_page = Login(self.driver)
        login_page.check_login()
        situation_func = Situation(self.driver)
        situation_func.check_situation()
        return


if __name__ == "__main__":
    unittest.main()

