from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from datetime import date
import json
import time

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def parse_json_data(self,json_file):
        with  open(json_file) as json_data:
            data = json.load(json_data)
        return data

    def get_element_list(self,locator,child_elem):
        elem = self.driver.find_element(*locator)
        elem_list = elem.find_elements_by_tag_name(child_elem)
        return elem_list


    def send_data(self, locator, data):
        data_field = self.driver.find_element(*locator)
        data_field.click()
        data_field.send_keys(Keys.CONTROL + 'a')
        data_field.send_keys(Keys.DELETE)
        data_field.send_keys(data)
        return
    

    def element_disable(self,locator):
        element = self.driver.find_element(*locator)
        return element.is_enabled()
    
    def get_calendar(self,month_year,prev_year,prev_month,next_year,next_month,date_calendar,prev_flag):
        today = date.today()
        current_date = today.strftime("%B %d, %Y")
        #date_list = [date.get_attribute('disabled') for date in self.get_element_list(date_calendar,"button")]
        #print(date_list)
        return



    def make_mouse_movement(self, locator):
        action = action_chains.ActionChains(self.driver)
        element = self.driver.find_element(*locator)
        action.move_to_element(element)
        action.perform()


    def element_click(self, locator):
        element = self.driver.find_element(*locator)
        assert(element.is_enabled())
        element.click()
        return

    def element_display(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def element_text(self,locator):
        return self.driver.find_element(*locator).text

    def select_dropdown(self,locator):
        self.element_click(locator)
        time.sleep(3)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()




