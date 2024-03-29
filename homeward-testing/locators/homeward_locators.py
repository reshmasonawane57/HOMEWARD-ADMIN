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
    logout_button = (By.XPATH, '//span[@class="log-out"]//parent::li')

    ################# Situation Page ####################

    whole_page = (By.XPATH, '/html/body')
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
    min_max_error = (By.XPATH, '//small[contains(@class,"text-danger")]')
    home_being_sold = (By.XPATH, '//div[contains(text(),"Home being sold")]//following::div[2]/input')
    outstanding_loan_amount = (By.XPATH, '//input[contains(@name,"outstanding_loan_amount")]')
    home_shopping_city = (By.XPATH, '//input[contains(@id,"shopping_location")]')
    home_value_opinion = (By.XPATH, '//input[contains(@name,"customer_home_value_opinion")]')
    min_price = (By.XPATH, '//input[contains(@name,"min_price")]')
    max_price = (By.XPATH, '//input[contains(@name,"max_price")]')
    offer_property_address = (By.XPATH, '//input[contains(@id,"offer_property_address")]')
    builders_name = (By.XPATH,'//input[contains(@name,"builders_company_name")]')
    builders_addr = (By.XPATH, '//input[contains(@id,"builders_address")]')

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

    ####################### Property Details ######################
    property_tab = (By.XPATH, '//a[contains(@id,"details-tab")]')
    bedroom_and_living_space  = (By.XPATH, '//div[contains(text(),"Bedrooms & Living spaces")]')
    bedroom_and_living_space1 = (By.XPATH, '//div[contains(text(), "Number of floors")]')
    bedroom_and_living_space2 = (By.XPATH, '//div[contains(text(), "Number of bedrooms")]')
    bedroom_and_living_space3 = (By.XPATH, '//div[contains(text(), "Master bedroom on main floor")]')
    bedroom_and_living_space4 = (By.XPATH, '//div[contains(text(), "Square footage")]')
    bedroom_and_living_space5 = (By.XPATH, '//div[contains(text(), "Permit status")]')
    bedroom_and_living_space6 = (By.XPATH, '//div[contains(text(), "Added square footage")]')
   
    kitchen_and_baths = (By.XPATH, '//div[contains(text(), "Kitchen & Baths")]')
    kitchen_and_baths1 = (By.XPATH, '//div[contains(text(), "Countertop type")]')
    kitchen_and_baths2 = (By.XPATH, '//div[contains(text(), "Appliance type")]')
    kitchen_and_baths3 = (By.XPATH, '//div[contains(text(), "Kitchen features")]')
    kitchen_and_baths4 = (By.XPATH, '//div[contains(text(), "Kitchen remodel")]')
    kitchen_and_baths5 = (By.XPATH, '//div[contains(text(), "Kitchen condition")]')
    kitchen_and_baths6 = (By.XPATH, '//div[contains(text(), "Master bathroom features")]')
    kitchen_and_baths7 = (By.XPATH, '//div[contains(text(), "Master bathroom remodel")]')
    kitchen_and_baths8 = (By.XPATH, '//div[contains(text(), "Master bathroom condition")]')
    kitchen_and_baths9 = (By.XPATH, '//div[contains(text(), "Full bathrooms")]')
    kitchen_and_baths10 = (By.XPATH, '//div[contains(text(), "Partial bathrooms")]')

    wall_and_flooring = (By.XPATH, '//div[contains(text(), "Walls & Flooring")]')
    wall_and_flooring1 = (By.XPATH, '//div[contains(text(), "Interior walls condition")]')
    wall_and_flooring2 = (By.XPATH, '//div[contains(text(), "Neutral paint colors in common area")]')
    wall_and_flooring3 =  (By.XPATH, '//div[contains(text(), "Floor type")]')
    wall_and_flooring4 =  (By.XPATH, '//div[contains(text(), "Hardwood condition")]')
    wall_and_flooring5 =  (By.XPATH, '//div[contains(text(), "Carpet condition")]')

    exteriors = (By.XPATH, '//div[contains(text(), "Exteriors")]')
    exteriors1 = (By.XPATH, '//div[contains(text(), "Front yard condition")]')
    exteriors2 = (By.XPATH, '//div[contains(text(), "Back yard condition")]')
    exteriors3 = (By.XPATH, '//div[contains(text(), "Exterior walls type")]')
    exteriors4 = (By.XPATH, '//div[contains(text(), "Sides with masonary")]')
    exteriors5 = (By.XPATH, '//div[contains(text(), "Roof age")]')
    exteriors6 = (By.XPATH, '//div[contains(text(), "Pool type")]')
    exteriors7 = (By.XPATH, '//div[contains(text(), "Garage spaces")]')
    
    other = (By.XPATH, '//div[text()="Other"]')
    other1 = (By.XPATH, '//div[contains(text(), "HVAC age")]')
    other2 = (By.XPATH, '//div[contains(text(), "Other home situations")]')
    other3 = (By.XPATH, '//div[contains(text(), "Property in floodzone")]')
    other4 = (By.XPATH, '//div[contains(text(), "Relationship to home")]')
    other5 = (By.XPATH, '//div[contains(text(), "Customer\'s home value opinion")]')

    number_of_floors = (By.XPATH, '//div[contains(text(),"Number of floors")]//following::div[5]')
    number_of_bedrooms = (By.XPATH, '//div[contains(text(),"Number of bedrooms")]//following::div[5]')
    master_bedroom_on_main_floor = (By.XPATH, '//div[contains(text(),"Master bedroom on main floor")]//following::div[5]')
    permit_status = (By.XPATH, '//div[contains(text(),"Permit status")]//following::div[5]')
    square_footage = (By.XPATH, '//input[contains(@name,"square_footage")]')
    added_square_footage = (By.XPATH, '//input[contains(@name,"size")]')

    countertop_type = (By.XPATH, '//div[contains(text(),"Countertop type")]//following::div[5]')
    appliance_type = (By.XPATH, '//div[contains(text(),"Appliance type")]//following::div[5]')
    kitchen_remodel = (By.XPATH, '//div[contains(text(),"Kitchen remodel")]//following::div[5]')
    kitchen_condition = (By.XPATH, '//div[contains(text(),"Kitchen condition")]//following::div[5]')
    master_bathroom_remodel = (By.XPATH, '//div[contains(text(),"Master bathroom remodel")]//following::div[5]')
    master_bathroom_condition = (By.XPATH, '//div[contains(text(),"Master bathroom condition")]//following::div[5]')
    full_bathrooms = (By.XPATH, '//div[contains(text(),"Full bathrooms")]//following::div[5]')
    partial_bathrooms = (By.XPATH, '//div[contains(text(),"Partial bathrooms")]//following::div[5]')

    interior_walls_condition = (By.XPATH, '//div[contains(text(),"Interior walls condition")]//following::div[5]')
    neutral_paint_colors_in_common_area = (By.XPATH, '//div[contains(text(),"Neutral paint colors in common area")]//following::div[5]')
    hardwood_condition = (By.XPATH, '//div[contains(text(),"Hardwood condition")]//following::div[5]')
    carpet_condition = (By.XPATH, '//div[contains(text(),"Carpet condition")]//following::div[5]')

    front_yard_condition = (By.XPATH, '//div[contains(text(),"Front yard condition")]//following::div[4]')
    back_yard_condition = (By.XPATH, '//div[contains(text(),"Back yard condition")]//following::div[5]')
    sides_with_masonary = (By.XPATH, '//div[contains(text(),"Sides with masonary")]//following::div[5]')
    roof_age = (By.XPATH, '//div[contains(text(),"Roof age")]//following::div[5]')
    pool_type = (By.XPATH, '//div[contains(text(),"Pool type")]//following::div[5]')
    garage_spaces = (By.XPATH, '//div[contains(text(),"Garage spaces")]//following::div[5]')

    hvac_age = (By.XPATH, '//div[contains(text(),"HVAC age")]//following::div[5]')
    property_in_floodzone = (By.XPATH, '//div[contains(text(),"Property in floodzone")]//following::div[5]')
    relationship_to_home = (By.XPATH, '//div[contains(text(),"Relationship to home")]//following::div[5]')
    customers_home_value_opinion = (By.XPATH, '//div[contains(text(), "Customer\'s home value opinion")]//following::input[contains(@name,"customer_home_value_opinion")]')

    image_header = (By.XPATH, '//div[contains(text(),"Images")]')
    image_parent = (By.XPATH, '//div[contains(@class,"p-30")]')
    image_child_element = (By.XPATH, '//div[@class="media-image"]')
    upload_button = (By.XPATH, '//button[contains(text(),"Upload images")]')
    upload_frame_title = (By.XPATH, '//h1[contains(text(),"Upload images")]')
    #cancel_button = (By.XPATH, '//h1[contains(text(),"Upload images")]//following::div[@class="col-md-6 text-right"]')
    browse_image = (By.XPATH,'//label[@class="dzu-inputLabel"]')
    upload_locator = (By.XPATH, '//label[@class="dzu-inputLabel"]/input')
    image_done = (By.XPATH, '//button[contains(text(),"Done")]')
    image_cancel = (By.XPATH, '//span[contains(@class,"dzu-previewButton")]')
    upload_image_cancel = (By.XPATH, '//h1[contains(text(),"Upload images")]//following::div[1]')
    image_type = (By.XPATH, '//div[contains(text(),"Select room")]')

    ###################################### Application ######################
    application_tab = (By.XPATH, '//a[@href="/applications"]//parent::li[@class="active"]')
    total_records = (By.XPATH, '//div[contains(@class,"records-found")]')
    pagination = (By.XPATH, '//ul[contains(@class,"custom-pagination")]')

