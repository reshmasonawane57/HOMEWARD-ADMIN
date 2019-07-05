import sys
sys.path.append('../pages')
sys.path.append('../locators')

from basepage import BasePage
from homeward_locators import Homeward_Locator
from datetime import date
import time

class Situation(BasePage):

    def validate_situation_page_data(self,application_data):
        try:
            title_bar = [elem.text for elem in self.get_element_list(Homeward_Locator.title_list,"li")]
            key_list = [ key for key in application_data["situation"]]
            #print(title_bar, application_data["situation"]["title_bar"])
            assert(self.element_text(Homeward_Locator.customer_status)== "Customer status")
            assert(self.element_text(Homeward_Locator.listing_details)== "Listing details")
            assert(self.element_text(Homeward_Locator.buying_details) == "Buying details")
            assert(self.element_text(Homeward_Locator.customer_status_field1) == "Customer reported stage")
            assert(self.element_text(Homeward_Locator.customer_status_field2) == "Target move in date")
            assert(self.element_text(Homeward_Locator.listing_details_field1) == "Home being sold")
            assert(self.element_text(Homeward_Locator.listing_details_field2) == "Outstanding loan amount")
            assert(self.element_text(Homeward_Locator.listing_details_field3) == "Home value opinion")
            assert(self.element_text(Homeward_Locator.buying_details_field1) == "Home shopping city")
            assert(self.element_text(Homeward_Locator.buying_details_field2) == "Price range")
            assert(self.element_text(Homeward_Locator.buying_details_field3) == "Offer property address")
        except:
            print("Error : Situation page data missing")

    def is_working_with_builder(self):
        try:
            assert(self.element_text(Homeward_Locator.buying_details_field4) == "Builder's name")
            assert(self.element_text(Homeward_Locator.buying_details_field5) == "Builder's address")
        except:
            print("Builder's name and Builder's address show Buying details")


    def check_Customer_status(self, application_data):
        try:
            self.select_dropdown(Homeward_Locator.customer_reported_stage,3)
            self.is_cta_confirm_cancel_bar()
            self.select_dropdown(Homeward_Locator.target_move_in_date,4)
            self.is_cta_confirm_cancel_bar()
    
            if(self.element_text(Homeward_Locator.customer_reported_stage) == "Working with a builder"):
                self.is_working_with_builder()
            if(self.element_text(Homeward_Locator.target_move_in_date) == "By a specific date"):
                self.is_by_specific_date()
        except:
            print("Error: Check customer status data")
        return

    def check_listing_details(self, application_data):
        try:
            self.send_data(Homeward_Locator.home_being_sold,"k")
            self.select_dropdown(Homeward_Locator.home_being_sold,3)
            self.is_cta_confirm_cancel_bar()
            self.send_data(Homeward_Locator.outstanding_loan_amount,"5654654")
            self.is_cta_confirm_cancel_bar()
            time.sleep(1)
            self.send_data(Homeward_Locator.home_value_opinion,"5654654")
            self.is_cta_confirm_cancel_bar()
        except:
            print("Error: Check listing details data")
        return

    def validate_min_max_value(self, min_data, max_data):
        self.send_data(Homeward_Locator.min_price,min_data)
        self.send_data(Homeward_Locator.max_price, max_data)
        self.is_cta_confirm_cancel_bar()
        min_value = self.get_attribute_value(Homeward_Locator.min_price)
        max_value = self.get_attribute_value(Homeward_Locator.max_price)
        if(min_data == max_data):
            error = self.element_text(Homeward_Locator.min_max_error)
            assert(error == "Values must be different")
        elif(min_data > max_data):
            error = self.element_text(Homeward_Locator.min_max_error)
            assert(error == "Min value must be lower than max value" or error == "Max value must be higher than min value")
        time.sleep(5)
        return

    def check_buying_details(self, application_data):
        try:
            self.send_data(Homeward_Locator.home_shopping_city,"p")
            self.select_dropdown(Homeward_Locator.home_shopping_city,3)
            self.is_cta_confirm_cancel_bar()
            self.validate_min_max_value("5000", "5000")
            self.validate_min_max_value("5000", "500")
            self.validate_min_max_value("5000", "50000")
            self.send_data(Homeward_Locator.offer_property_address,"5")
            self.select_dropdown(Homeward_Locator.offer_property_address,3)
            self.is_cta_confirm_cancel_bar()
            self.send_data(Homeward_Locator.builders_name,"jdsfbk")
            self.get_page_end(Homeward_Locator.whole_page)
            time.sleep(3)
            self.send_data(Homeward_Locator.builders_addr,"j")
            time.sleep(3)
            self.get_page_end(Homeward_Locator.whole_page)
            self.select_dropdown(Homeward_Locator.builders_addr,3)
            self.get_page_end(Homeward_Locator.whole_page)
            self.is_cta_confirm_cancel_bar()
            time.sleep(5)
        except:
            print("Error: check buying details data")
        return

    def validate_data(self):
        try:
            address = self.driver.find_element(*Homeward_Locator.home_being_sold).get_attribute("value")
            addr_title = self.element_text(Homeward_Locator.page_header)
            assert(addr_title == address)
        except:
            print("Error : Address Title")
        return


    def check_situation_page(self, application_data):
        try:
            self.make_mouse_movement(Homeward_Locator.subject_property)
            time.sleep(3)
            assert(self.driver.find_element(*Homeward_Locator.subject_property_tab).text == "Property overview")
            assert( "show" in self.driver.find_element(*Homeward_Locator.subject_property_tab).get_attribute("class"))
            self.check_Customer_status(application_data)
            self.check_listing_details(application_data)
            self.check_buying_details(application_data)
            time.sleep(3)
            self.validate_data()
        except:
            print("Error : Situation page")
        return


    def check_situation(self):
        application_data =  self.parse_json_data("../test_data/application_page_data.json")
        self.element_click(Homeward_Locator.table_row)
        self.validate_situation_page_data(application_data)
        self.check_situation_page(application_data)
        time.sleep(1)
        return

