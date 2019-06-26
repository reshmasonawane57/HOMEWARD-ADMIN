from selenium.webdriver.common.by import By

class Homeward_Locator(object):
    
    ####### Login page ##########
    login_title = (By.XPATH,'//div[contains(@class,"login-panel")]/h3')
    username_header = (By.XPATH, '//label[contains(text(),"Email address")]')
    username = (By.XPATH, '//input[contains(@type,"email")]')
    password_header = (By.XPATH, '//label[contains(text(),"Password")]')
    password = (By.XPATH, '//input[contains(@type,"password")]')
    submit_button = (By.XPATH, '//button[contains(text(),"Log in")]')
    err_msg = (By.XPATH, '//div[contains(@class,"alert-danger")]')

    ################# Situation Page ####################

    table_row = (By.XPATH, '//table[contains(@class,"table")]/tbody/tr[2]')
    page_header = (By.XPATH, '//h1[contains(@class,"page-title")]')
    customer_reported_stage = (By.XPATH, '//div[contains(text(),"Customer reported stage")]//following::div[4]')
    text_customer_reported_stage = (By.XPATH, '//div[contains(text(),"Customer reported stage")]//following::div[6]')
    title_list = (By.XPATH,'//ul[contains(@id,"myTab")]')
    situation_tab = (By.XPATH, '//a[contains(@id,"situation-tab")]')
    subject_property_tab = (By.XPATH, '//div[contains(@class,"_react_component")]')
    subject_property = (By.XPATH, '//div[contains(@class,"_react_component")]//following::li[1]')
    customer_status = (By.XPATH, '//div[contains(text(),"Customer status")]')
    listing_details = (By.XPATH, '//div[contains(text(),"Listing details")]')
    buying_details = (By.XPATH, '//div[contains(text(),"Buying details")]')

    customer_status_field1 = (By.XPATH, '//div[contains(text(),"Customer reported stage")]')
    customer_status_field2 = (By.XPATH, '//div[contains(text(),"Target move in date")]')
    customer_status_field3 = (By.XPATH, '//div[contains(text(),"Move by date")]')
    customer_reported_stage = (By.XPATH, '//div[contains(text(),"Customer reported stage")]//following::div[6]')
    target_move_in_date = (By.XPATH, '//div[contains(text(),"Target move in date")]//following::div[6]')
    listing_details_field1 = (By.XPATH, '//div[contains(text(),"Home being sold")]')
    listing_details_field2 = (By.XPATH, '//div[contains(text(),"Outstanding loan amount")]')
    listing_details_field3  = (By.XPATH, '//div[contains(text(),"Home value opinion")]')
    buying_details_field1 = (By.XPATH, '//div[contains(text(),"Home shopping city")]')
    buying_details_field2 = (By.XPATH, '//div[contains(text(),"Price range")]')
    buying_details_field3 = (By.XPATH, '//div[contains(text(),"Offer property address")]')
    buying_details_field4 = (By.XPATH, '//div[contains(text(),"Builder\'s name")]')
    buying_details_field5 = (By.XPATH, '//div[contains(text(),"Builder\'s address")]')
    home_being_sold = (By.XPATH, '//div[contains(text(),"Home being sold")]//following::div[2]/input')
    outstanding_loan_amount = (By.XPATH, '//input[contains(@name,"outstanding_loan_amount")]')
    home_value_opinion = (By.XPATH, '//input[contains(@name,"customer_home_value_opinion")]')

    cta_footer_bar = (By.XPATH, '//div[contains(@class,"form-grey-panel-button")]')
    cancel_button = (By.XPATH, '//button[contains(text(),"Cancel")]')
    confirm_button = (By.XPATH, '//button[contains(text(),"Confirm")]')

    move_by_date = (By.XPATH, '//input[contains(@name,"move_by_date")]')
    clear_date = (By.XPATH, '//button[contains(@class,"react-date-picker__clear-button")]')
    calendar = (By.XPATH, '//button[contains(@class,"react-date-picker__calendar-button")]')
    month_and_year = (By.XPATH, '//button[contains(@class,"react-calendar__navigation__label")]')
    prev_year = (By.XPATH, '//button[contains(@class,"react-calendar__navigation__arrow react-calendar__navigation__prev2-button")]')
    prev_month = (By.XPATH, '//button[contains(@class,"react-calendar__navigation__arrow react-calendar__navigation__prev-button")]')
    next_year = (By.XPATH, '//button[contains(@class,"react-calendar__navigation__arrow react-calendar__navigation__next2-button")]')
    next_month = (By.XPATH, '//button[contains(@class,"react-calendar__navigation__arrow react-calendar__navigation__next-button")]')
    date_calendar = (By.XPATH, '//div[contains(@class,"react-calendar__month-view__days")]')
