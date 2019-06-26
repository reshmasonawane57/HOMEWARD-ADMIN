import sys
sys.path.append('../page')
sys.path.append('../locators')

from basepage import BasePage
from homeward_locators import Homeward_Locator
import time

class Login(BasePage):

    def check_negative_login(self, data):
        self.send_data(Homeward_Locator.username, "shashank.n@amazatic.com")
        self.send_data(Homeward_Locator.password, "shashank")
        self.element_click(Homeward_Locator.submit_button)
        assert(data["login_errmsg"] == self.driver.find_element(*Homeward_Locator.err_msg).text)
        #self.driver.execute_script('window.localStorage.clear();')
        time.sleep(3)
        #self.driver.execute_script("location.reload(true);")
        return

    def check_email_error(self, data):
        self.send_data(Homeward_Locator.password, "shashank")
        time.sleep(3)
        self.element_click(Homeward_Locator.submit_button)
        assert(data["email_errmsg"] == self.driver.find_element(*Homeward_Locator.err_msg).text)
        time.sleep(3)

    def check_password_error(self, data):
        self.send_data(Homeward_Locator.username, "shashank.n@amazatic.com")
        time.sleep(3)
        self.element_click(Homeward_Locator.submit_button)
        assert(data["password_errmsg"] == self.driver.find_element(*Homeward_Locator.err_msg).text)
        time.sleep(3)


    def check_login(self):
        data = self.parse_json_data("login_page.json")
        assert(data["login_header"] == self.driver.find_element(*Homeward_Locator.login_title).text)
        assert(data["username"] == self.driver.find_element(*Homeward_Locator.username_header).text)
        assert(data["Password"] == self.driver.find_element(*Homeward_Locator.password_header).text)
        self.check_email_error(data)
        self.check_password_error(data)
        self.check_negative_login(data)
        self.send_data(Homeward_Locator.username, "shashank.n@amazatic.com")
        self.send_data(Homeward_Locator.password, "shashank123")
        self.element_click(Homeward_Locator.submit_button)
        time.sleep(4)
        self.element_click(Homeward_Locator.table_row)
        time.sleep(3)
        return


