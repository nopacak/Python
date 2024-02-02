from selenium.webdriver.support.ui import Select
from selenium_functions import *
from config import *
import time


# Defining each step of the process as a function (task) 


# Step 1: Open the website
def open_the_website():
    log_step("Opening the website", log_file)
    """Navigates to the given URL"""
    open_browser('url of the website')
    log_step("Website opened successfully", log_file)



# Step 2: Log in to the website
def log_in():
    """Fills in the login form and clicks the 'Log in' button"""
    log_step("Logging in", log_file)
    global user, secret
    wait_and_input_text("id", user)
    input_text("name", secret)
    click_element("id")
    log_step("Logged in successfully", log_file)



# Step 3: Navigate to the data input page
def navigate_website_to_data_input(offer_id):
    xpath = ['list of several xpaths']
    
    for i in xpath:
        wait_and_click(i)

    if is_element_visible_by_text_attribute("some warning message"):
        set_status_column(offer_id, "Please process manually")
        return True
    return False



# Step 4: Calculate the insurance premium (input all data and then click on "Calculate" button)
def calculate_insurance_premium(offer_data):
    
    """Fills in the form to calculate the insurance premium"""

    log_step("Starting 'Calculate the insurance premium' task", log_file)
    address = ', '.join(filter(None, [offer_data.street, offer_data.city, offer_data.zip_code]))
    contractor_address = ', '.join(filter(None, [offer_data.contractor_street, offer_data.contractor_city, offer_data.contractor_zip_code]))
    

    # log the offer that is currently being processed
    log_step(f"""Processing data for offer: {offer_id} \n 
             Owner: {offer_data.firstName} {offer_data.lastName} \n
             Owner oib: {offer_data.oib} \n
             Address: {offer_data.full_address} \n
             Contractor: {offer_data.contractor_firstName} {offer_data.contractor_lastName} \n
             Contractor oib: {offer_data.contractor_oib} \n
             Contractor address: {offer_data.contractor_full_address} \n
             Chassis: {offer_data.chassis} \n
             Registration: {offer_data.reg} \n
             Leasing: {offer_data.leasing} \n
             Kasko: {offer_data.only_kasko} \n
             Bonus: {offer_data.bonus} \n""", log_file)
    

    # Check whether there is a chassis number in database, if not, use registration number
    if str(offer_data.chassis) != "":
        wait_and_click('xpath')
        wait_and_input_text('id', offer_data.chassis)
        browser.press_keys("id", "ENTER")
        
    else:
        wait_and_input_text("id", offer_data.reg)
        browser.press_keys("id", "ENTER")

    #10 seconds pause to allow the page to load
    time.sleep(10)
    
    # Check if the insurance policy is sold
    if is_element_visible(get_text_xpath("sold insurance policy")):
        set_status_column(offer_id, str(browser.get_element_attribute(get_text_xpath("sold insurance policy"), 'textContent')).split(".")[0])
        return True
    
    browser.wait_until_element_is_visible('xpath', timeout=90)

    # frame_1 is a boolean variable that will be used to check if the 1st frame with elements has been selected
    frame_1 = False

    # Check if the registration number matches the one in database, if not, correct it
    if (str(browser.get_element_attribute('xpath', "textContent"))[0:2] != str(offer_data.reg_prefix)) and (str(browser.get_element_attribute('xpath', "textContent")) != "BEZ TABLICE"):
        click_element('xpath')
        browser.wait_until_element_is_visible('xpath', timeout=90)
        browser.select_frame('xpath')

        table_xpath = 'xpath'

        if offer_data.reg_prefix != offer_data.reg:
            wait_and_input_text("id, reg)
            click_element('xpath')
            click_element('xpath')
            click_element('xpath')

        
        elif is_element_visible(table_xpath) and (str(browser.get_element_attribute(table_xpath, "textContent"))[0:2] == offer_data.reg_prefix):
            click_element('xpath')
            click_element('xpath')

        else:
            wait_and_input_text("id", offer_data.reg)
            click_element('xpath')
            click_element('xpath')
            browser.wait_until_element_is_visible('xpath', timeout=90)
            text_content = str(browser.get_element_attribute('xpath', "textContent"))
            option, vehicle_type = text_content.split(" - ")
            input_text('xpath', option)
            wait_and_click(get_text_xpath(vehicle_type))
            click_element('xpath')


        browser.unselect_frame()
        frame_1 = True

    close_all()

    # Selecting the correct option for leasing based on the database value
    if offer_data.leasing:
        click_element('xpath')
    else:
        click_element('xpath')

    
    # Selecting the correct option for kasko based on the database value
    if offer_data.only_kasko:
        if is_element_visible('xpath'):
            click_element('xpath')
    else:
        if is_element_visible('xpath'):
            click_element('xpath')
        
    # 5 seconds pause to allow the page to load
    time.sleep(5)

    # Check if the input field for oib is visible
    if is_element_visible('xpath'):
        if offer_data.leasing:
            input_text('xpath', offer_data.contractor_oib)
            click_element('id')
        else:
            input_text('xpath', offer_data.oib)
            click_element('id')

    # 2 seconds pause to allow the page to load
    time.sleep(2)

    #selection window - it appears sometimes when there are multiple results for the entered oib
    if is_element_visible('xpath'):
        click_element('xpath')
    
    # Defining a function to change the oib if it doesn't match the one in database
    def change_oib(personal_identification_number):
        input_text('id', personal_identification_number)
        wait_and_input_text('xpath', personal_identification_number)
        browser.press_keys('xpath', "ENTER")
        wait_and_click('xpath')
        click_element('xpath')
        wait_and_click('xpath')
        browser.unselect_frame()
        
    oib_xpath = 'xpath'
    browser.wait_until_element_is_visible(oib_xpath, timeout=90)
    coins_oib = str(browser.get_element_attribute(oib_xpath, 'textContent'))
    
    # Check if the oib matches the one in database, if not, correct it
    if offer_data.leasing and (coins_oib != str(offer_data.contractor_oib)):
        click_element('xpath')
        frame_2 = False
        if frame_1:
            browser.wait_until_element_is_visible('xpath', timeout=90)
            browser.select_frame('xpath')
            frame_2 = True
        else:
            browser.wait_until_element_is_visible('xpath', timeout=90)
            browser.select_frame('xpath')
        change_oib(offer_data.contractor_oib)


    elif not offer_data.leasing and (coins_oib != str(offer_data.oib)):
        click_element('xpath')
        frame_2 = False
        if frame_1:
            browser.wait_until_element_is_visible('xpath', timeout=90)
            browser.select_frame('xpath')
            frame_2 = True
        else:
            browser.wait_until_element_is_visible('xpath', timeout=90)
            browser.select_frame('xpath')
        change_oib(offer_data.oib)
    
    browser.wait_until_element_is_visible(oib_xpath, timeout=90)


    time.sleep(5)
    # Close all messages that might appear and obstruct other elements
    close_all()

    def get_xpath(row, column):
        return f'//*[@id="some_id"]/tbody/tr[{row}]/td[{column}]'

    def check_zip_code_mismatch(zip_code, rows):
        for row in rows:
            label = str(browser.get_element_attribute(get_xpath(row, 1), 'textContent'))
            value = str(browser.get_element_attribute(get_xpath(row, 2), 'textContent'))
            if label == "ZIP Code" and value != str(zip_code):
                return True
        return False
    rows_to_check = [5, 6]  

    if offer_data.leasing and check_zip_code_mismatch(offer_data.contractor_zip_code,rows_to_check):
        set_status_column(offer_id, "Address data does not match.")
        return True


    elif not offer_data.leasing and check_zip_code_mismatch(offer_data.zip_code,rows_to_check):
        set_status_column(offer_id, "Address data does not match.")
        return True




    if str(offer_data.bonus) not in ("50", "0"):
        click_element('xpath')
        browser.wait_until_element_is_visible('xpath', timeout=90)
        browser.select_frame('xpath')
        click_element('xpath)
        browser.wait_until_element_is_visible('xpath', timeout=90)
        if str(offer_data.bonus) == "10":
            click_element('xpath')
        elif str(offer_data.bonus) == "15":
            click_element('xpath')
        elif str(offer_data.bonus) == "20":
            click_element('xpath')
        elif str(offer_data.bonus) == "25":
            click_element('xpath')
        elif str(offer_data.bonus) == "30":
            click_element('xpath')
        elif str(offer_data.bonus) == "35":
            click_element('xpath')
        elif str(offer_data.bonus) == "40":
            click_element('xpath')
        elif str(offer_data.bonus) == "45":
            click_element('xpath')
        click_element('xpath')

        if is_element_visible_by_text_attribute("Some warning message"):
            click_element('xpath')
        if str(offer_data.bonus) == "" or None:
            print("Bonus unknown")
        browser.unselect_frame()


    if is_element_visible('xpath'):
        click_element('xpath')

    if is_element_visible('id'):
        click_element('xpath')
        browser.wait_until_element_is_visible(get_text_xpath("Some value"), timeout=60)
        input_text('id', offer_data.reg_prefix)
        time.sleep(5)
        browser.press_keys('id', "ENTER")
        time.sleep(5)
        click_element('xpath')

    time.sleep(5)
    # Close all messages that might appear and obstruct other elements
    close_all()

    # Wait for the "Izracun" button to appear and click on it
    wait_and_click('id')

    log_step("All data imported correctly", log_file)
    return False



# Step 5: Show the calculated premium and available discounts
def show_premium(offer_id, bonus):
    """Show the calculated premium and available discounts"""
    time.sleep(15)
    #Un-click whatever is clicked within a container
    browser.wait_until_element_is_visible('xpath', timeout=60)
    checked_elements = browser.find_elements('xpath//*[contains(@class, "mdl-switch-item__checked")]')
    for element in checked_elements:
        click_element(element)

    log_step("Starting 'Calculating insurance premium' task", log_file)
    insurance_premium_xpath = 'xpath'
    browser.wait_until_element_is_visible(insurance_premium_xpath, timeout=60)
    element = str(browser.get_element_attribute(insurance_premium_xpath, "textContent")).replace(",", ".")

    bonus_multipliers = {
        "10": 10,
        "15": 6.67,
        "20": 5,
        "25": 4,
        "30": 3.33,
        "35": 2.86,
        "40": 2.5,
        "45": 2.22,
        "50": 2,
        "0": 2
    }

    # Convert bonus to string and get the corresponding multiplier
    multiplier = bonus_multipliers.get(str(bonus))

    # Calculate the insurance premium if the bonus is valid
    if multiplier is not None:
        insurance_premium = float(element) * multiplier
        print(insurance_premium)
    else:
        print("Invalid bonus value")


    if is_element_visible('id):
        # Retrieve all options from the dropdown as WebElement objects
        options_1 = Select(browser.find_element('id')).options
        # Get the last option's value
        commercial_discount = float(options_1[-1].get_attribute('value'))
    else:
        commercial_discount = ""

    if is_element_visible('id'):
        #repeat the same for the second dropdown
        options_2 = Select(browser.find_element('id')).options
        advisor_discount = float(options_2[-1].get_attribute('value'))
    else:
        advisor_discount = ""


    df = pd.read_csv(csv_file)
    # Update the DataFrame
    df.loc[df['ID'] == offer_id, 'Column1'] = insurance_premium
    df.loc[df['ID'] == offer_id, 'Column2'] = commercial_discount
    df.loc[df['ID'] == offer_id, 'Column3'] = advisor_discount

    grouped = df.groupby('Column1')

    # Fill missing values for each group
    df['Column1'] = grouped['Column1'].transform(lambda x: x.ffill().bfill())
    df['Column2'] = grouped['Column2'].transform(lambda x: x.ffill().bfill())
    df['Column3'] = grouped['Column3'].transform(lambda x: x.ffill().bfill())

    df.loc[df['ID'] == offer_id, 'Status'] = "Success"
    df["Status"] = df["Status"].astype(str)
    # Save the updated DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)

    log_step("Insurance premium calculated successfully", log_file)


# Step 6: Close the browser
log_step("Closing the browser", log_file)
close_browser()
log_step("Browser closed successfully, process completed successfully", log_file)
