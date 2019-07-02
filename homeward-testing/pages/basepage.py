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

    def get_page_end(self, locator):
        self.driver.find_element(*locator).send_keys(Keys.END)
        return

    def get_page_up(self, locator):
        self.driver.find_element(*locator).send_keys(Keys.HOME)
        return
    

    def element_disable(self,locator):
        element = self.driver.find_element(*locator)
        return element.is_enabled()

    """def check_disable_day(self,date_calendar,date_list,current_day):
        return
    """

    def get_attribute_value(self, locator):
        return self.driver.find_element(*locator).get_attribute("value")

    def calendar_functionality(self,next_month,next_year,prev_month,prev_year):
        assert(self.driver.find_element(*prev_year).get_attribute("disabled"))
        assert(self.driver.find_element(*prev_month).get_attribute("disabled"))
        assert(self.element_disable(next_year))
        assert(self.element_disable(next_month))
        self.element_click(next_year)
        time.sleep(3)
        self.element_click(prev_year)
        time.sleep(3)
        self.element_click(next_month)
        time.sleep(3)
        self.element_click(prev_month)
        time.sleep(3)
        return
    
    def get_calendar(self,month_year,prev_year,prev_month,next_year,next_month,date_calendar,prev_flag):
        today = date.today()
        current_date = today.strftime("%B %d, %Y")
        list_of_date = [date for date in self.get_element_list(date_calendar,"button")]
        date_list = [(date.text,date.get_attribute('disabled')) for date in self.get_element_list(date_calendar,"button")]
        calendar_date = self.element_text(month_year).split()
        current_month = current_date.split()[0]
        current_day = current_date.split()[1]
        current_year = current_date.split()[2]
        assert(current_month==calendar_date[0])
        assert(current_year==calendar_date[1])
        self.calendar_functionality(next_month,next_year,prev_month,prev_year)
        list_of_date = self.get_element_list(date_calendar, "button")
        day_index = [ day for day in date_list if "true" not in day]
        date_index = date_list.index(day_index[0])
        list_of_date[date_index].click()
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

    def select_dropdown(self,locator,n_dropdown):
        self.element_click(locator)
        time.sleep(3)
        action = action_chains.ActionChains(self.driver)
        for i in range(n_dropdown):
            action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()




