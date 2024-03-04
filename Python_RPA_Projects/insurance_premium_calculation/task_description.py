from selenium.webdriver.support.ui import Select
from .selenium_functions import *
import time
import base64
import datetime
import pandas as pd

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_file = f"logs/robot_{date}.log"

# Decode login credentials from base64
user = base64.b64decode("user").decode('utf-8')
secret = base64.b64decode("passcode").decode('utf-8')

# Declare some xpath variables
cvh_xpath = 'xpath=//*[@id="report_cvhPregledReg"]/tbody/tr[2]/td[2]/span'
oib_input_field = 'xpath=//*[@id="P2000_32_10_OIB_X"]'
oib_xpath = 'xpath=//*[@id="report_rgn_uloga"]/tbody/tr[1]/td[2]'


# Defining a function to change the oib if it doesn't match the one in database
def change_oib(personal_identification_number):
    input_text('id=P2200_32_10_OIB', personal_identification_number)
    browser.press_keys('xpath=//*[@id="snkLovSearch"]', "ENTER")
    wait_and_click('xpath=//*[@id="mlov_tbl_stranka"]/tbody/tr')
    click_element('xpath=//*[@id="sLovBtnGetVals"]')
    wait_and_click('xpath=//*[@id="B263642850160457003"]/span[3]')
    browser.unselect_frame()

# Defining a function to set the field "registarsko područje" to the correct value
def set_registarsko_područje(reg_prefix):
    click_element('xpath=//*[@id="P2000_32_10_RGP_holder"]/tbody/tr/td/span')
    browser.wait_until_element_is_visible(get_text_xpath("-- Isprazni vrijednost --"), timeout=60)
    input_text('id=mlovSearch', reg_prefix)
    browser.press_keys('id=mlovSearch', "ENTER")
    click_element('xpath=//*[@id="ui-id-2"]/div[2]/table/tbody/tr[2]/td[2]')

# Defining a function to set the bonus to the correct value
def set_bonus(df, bonus):
    if str(bonus) == "" or None:
        df["Status"] = "Bonus nije naveden u bazi. Molim ručnu provjeru."
        return df, True    
    click_element('xpath=//*[@id="btnPrijenosPS"]/span[3]')
    browser.wait_until_element_is_visible('xpath://iframe[@title="Prijenos PS"]', timeout=90)
    browser.select_frame('xpath://iframe[@title="Prijenos PS"]')
    click_element('xpath=//*[@id="P2109_PS_holder"]/tbody/tr/td/span')
    browser.wait_until_element_is_visible('xpath=//*[@id="ui-id-4"]/div[2]/table/tbody/tr[1]', timeout=90)

    # Convert bonus to integer for calculation
    bonus_value = int(bonus)
    # Calculate the row index based on the bonus value
    row_index = 14 - (bonus_value // 5)
    # Click the element using the calculated row index
    click_element(f'xpath=//*[@id="ui-id-5"]/div[2]/table/tbody/tr[{row_index}]')
    click_element('xpath=//*[@id="B263700687058067301"]')

    if is_element_visible_by_text_attribute("Premijski stupanj mora biti 50."):
        click_element('xpath=//*[@id="closeModal"]/span[2]')
        df["Bonus"] = "50"
    browser.unselect_frame()
    return df, False


# Defining functions for checking the zip code mismatch
def get_xpath(row, column):
    return f'//*[@id="report_rgn_uloga"]/tbody/tr[{row}]/td[{column}]'

def check_zip_code_mismatch(zip_code, rows):
    for row in rows:
        label = str(browser.get_element_attribute(get_xpath(row, 1), 'textContent'))
        value = str(browser.get_element_attribute(get_xpath(row, 2), 'textContent'))
        if label == "Poštanski broj" and value != str(zip_code):
            return True
    return False

# Defining each step of the process as a function (task) 
    
# Step 1: Open the Crosig website
def open_insurance_website():
    """Navigates to the given URL"""
    open_browser('website url')


# Step 2: Log in to the Crosig website
def log_in(df):
    """Fills in the login form and clicks the 'Log in' button"""
    global user, secret
    wait_and_input_text("id=P101_USERNAME", user)
    input_text("name=P101_PASSWORD", secret)
    click_element("id=P101_LOGIN")
    if is_element_visible('xpath=//*[@id="jGrowl"]/div[2]'):
        df["Status"] = "Prijavni podaci nisu ispravni. Molim izmjenu prijavnih podataka (korisničko ime/lozinka)."
        return df, True
    return df, False


# Step 3: Navigate to the data input page
def navigate_website_to_data_input(df):
    xpath = ['xpath=//*[@id="R54138048149159531"]/div/ul/li[1]/a/div[1]',
        'xpath=//*[@id="R86718136660563338"]/div/ul/li[2]/a',
        'xpath=//*[@id="R86861457409699763"]/ul/li[1]/a',
        'xpath=//*[@id="R270691103014061901"]/div[2]/div/h1',
        'xpath=//*[@id="btnNoviAO"]/span[3]',
        'xpath=//*[@id="btnRetailAO"]/span[3]']
    
    for i in xpath:
        wait_and_click(i)

    if is_element_visible_by_text_attribute("AJAX"):
        df["Status"] = "Greška u aplikaciji coins. Molim ručni izračun."
        return df, True
    return df, False



# Step 4: Calculate the insurance premium (input all data and then click on "Izracun" button)
def calculate_insurance_premium(df,offer_data):
    
    """Fills in the form to calculate the insurance premium"""

    # Check whether there is a chassis number in database, if not, use registration number
    if str(offer_data.chassis) != "":
        wait_and_click('xpath=//*[@id="P2000_BEZ_REG"]/div/div/div[2]')
        wait_and_input_text('id=P2000_W1_0_SASIJA', offer_data.chassis)
        browser.press_keys("id=P2000_W1_0_SASIJA", "ENTER")
        
    else:
        wait_and_input_text("id=P2000_W1_0_REGISTRACIJA", offer_data.reg)
        browser.press_keys("id=P2000_W1_0_REGISTRACIJA", "ENTER")

    #10 seconds pause to allow the page to load
    time.sleep(10)
    
    # Check if the insurance policy is sold
    if is_element_visible(get_text_xpath("nije kandidat za obnovu")):
        df["Status"] = str(browser.get_element_attribute(get_text_xpath("nije kandidat za obnovu"), 'textContent')).split(".")[0]
        return df, True
    
    browser.wait_until_element_is_visible('xpath=//*[@id="report_rgn_vozilo"]/tbody/tr[1]/td[2]', timeout=90)

    # frame_1 is a boolean variable that will be used to check if the 1st frame with elements has been selected
    frame_1 = False

    # Check if the registration number matches the one in database, if not, correct it
    if (str(browser.get_element_attribute('xpath=//*[@id="report_rgn_vozilo"]/tbody/tr[1]/td[2]', "textContent"))[0:2] != str(offer_data.reg_prefix)) and (str(browser.get_element_attribute('xpath=//*[@id="report_rgn_vozilo"]/tbody/tr[3]/td[2]', "textContent")) != "BEZ TABLICE"):
        click_element('xpath=//*[@id="btnIzmjeniVozilo"]/span[3]')
        browser.wait_until_element_is_visible('xpath://iframe[@title="Vozilo"]', timeout=90)
        browser.select_frame('xpath://iframe[@title="Vozilo"]')
        time.sleep(10)

        if offer_data.reg_prefix != offer_data.reg:
            wait_and_input_text("id=P2100_REGISTRACIJA", offer_data.reg)
            click_element('xpath=//*[@id="P2100_32_10_VRG"]')
            click_element('xpath=//*[@id="P2100_32_10_VRG"]/option[2]')
            click_element('xpath=//*[@id="B263414227328991924"]')

        
        elif is_element_visible(cvh_xpath) and (str(browser.get_element_attribute(cvh_xpath, "textContent"))[0:2] == offer_data.reg_prefix):
            click_element('xpath=//*[@id="btnCvhVozilo"]')
            click_element('xpath=//*[@id="B263414227328991924"]')

        else:
            wait_and_input_text("id=P2100_REGISTRACIJA", offer_data.reg)
            click_element('xpath=//*[@id="P2100_32_10_VRG"]')
            click_element('xpath=//*[@id="P2100_32_10_VRG"]/option[6]')
            browser.wait_until_element_is_visible('xpath=//*[@id="report_vzlPregledReg"]/tbody/tr[3]/td[2]/span', timeout=90)
            text_content = str(browser.get_element_attribute('xpath=//*[@id="report_vzlPregledReg"]/tbody/tr[3]/td[2]/span', "textContent"))
            option, vehicle_type = text_content.split(" - ")
            input_text('xpath=//*[@id="P2100_VSV_ID"]', option)
            time.sleep(10)
            wait_and_click(get_text_xpath(vehicle_type))
            time.sleep(10)
            click_element('xpath=//*[@id="B263414227328991924"]')


        browser.unselect_frame()
        frame_1 = True
        
    # Close all messages that might appear and obstruct other elements
    close_all()

    # Selecting the correct option for kasko based on the database value
    if offer_data.only_kasko:
        if is_element_visible('xpath=//*[@id="P2000_32_10_IND_AO_AK"]/div/div/div[1]'):
            click_element('xpath=//*[@id="P2000_32_10_IND_AO_AK"]/div/div/div[1]')
    else:
        if is_element_visible('xpath=//*[@id="P2000_32_10_IND_AO_AK"]/div/div/div[2]'):
            click_element('xpath=//*[@id="P2000_32_10_IND_AO_AK"]/div/div/div[2]')

    # Selecting the correct option for leasing based on the database value and check if the input field for oib is visible
    if offer_data.leasing:
        click_element('xpath=//*[@id="P2000_32_10_LSG"]/div/div/div[1]/label')
        if is_element_visible(oib_input_field):
            input_text(oib_input_field, offer_data.contractor_oib)
            click_element('id=P2000_32_10_OIB_X_OPEN_LOV')
    else:
        click_element('xpath=//*[@id="P2000_32_10_LSG"]/div/div/div[2]/label')
        if is_element_visible(oib_input_field):
            input_text(oib_input_field, offer_data.oib)
            click_element('id=P2000_32_10_OIB_X_OPEN_LOV')


    # Close all messages that might appear and obstruct other elements
    close_all()

    #selection window - it appears sometimes when there are multiple results for the entered oib
    type_key = "contractor_type" if offer_data.leasing else "customer_type"
    type_value = getattr(offer_data, type_key)

    if is_element_visible('xpath=//*[@id="P2000"]/div[6]'):
        if type_value == "person" and is_element_visible_by_text_attribute("Fizička"):
            click_element('xpath=//*[@id="mlov_tbl_stranka"]/tbody/tr/td[6]')
            print_action = "Odabrao sam fizičku osobu."
        elif type_value == "company" and is_element_visible_by_text_attribute("Obrtnik"):
            browser.scroll_element_into_view(get_text_xpath("Obrtnik"))
            click_element(get_text_xpath("Obrtnik"))
            print_action = "Odabrao sam obrtnika."
        else:
            df["Status"] = "Nije moguće odrediti tip korisnika. Molim ručnu provjeru."
            return df, True

        if print_action:
            #print(print_action)
            click_element('xpath=//*[@id="sLovBtnGetVals"]')

    
    browser.wait_until_element_is_visible(oib_xpath, timeout=90)
    coins_oib = str(browser.get_element_attribute(oib_xpath, 'textContent'))
    
    # Check if the oib matches the one in database, if not, correct it
    frame_2 = False
    if offer_data.leasing and (coins_oib != str(offer_data.contractor_oib)):
        click_element('xpath=//*[@id="podaci_uloge"]')
        if frame_1:
            browser.wait_until_element_is_visible('xpath=//*[@id="apex_dialog_2"]/iframe', timeout=90)
            browser.select_frame('xpath=//*[@id="apex_dialog_2"]/iframe')
            frame_2 = True
        else:
            browser.wait_until_element_is_visible('xpath=//*[@id="apex_dialog_1"]/iframe', timeout=90)
            browser.select_frame('xpath=//*[@id="apex_dialog_1"]/iframe')
        change_oib(offer_data.contractor_oib)


    elif not offer_data.leasing and (coins_oib != str(offer_data.oib)):
        click_element('xpath=//*[@id="podaci_uloge"]')
        
        if frame_1:
            browser.wait_until_element_is_visible('xpath=//*[@id="apex_dialog_2"]/iframe', timeout=90)
            browser.select_frame('xpath=//*[@id="apex_dialog_2"]/iframe')
            frame_2 = True
        else:
            browser.wait_until_element_is_visible('xpath=//*[@id="apex_dialog_1"]/iframe', timeout=90)
            browser.select_frame('xpath=//*[@id="apex_dialog_1"]/iframe')
        change_oib(offer_data.oib)

    
    browser.wait_until_element_is_visible(oib_xpath, timeout=90)

    time.sleep(5)
    
    # Close all messages that might appear and obstruct other elements
    close_all()

    rows_to_check = [5, 6]  

    if offer_data.leasing and check_zip_code_mismatch(offer_data.contractor_zip_code,rows_to_check):
        df["Status"] = "Adresa ugovaratelja se ne podudara sa kpass-om."
        return df, True

    elif not offer_data.leasing and check_zip_code_mismatch(offer_data.zip_code,rows_to_check):
        df["Status"] = "Adresa korisnika se ne podudara sa kpass-om."
        return df, True
    
    if str(offer_data.bonus) not in ("50", "0"):
        df, success = set_bonus(df, offer_data.bonus)
        if success:
            return df, True

    if is_element_visible('xpath=//*[@id="P2000_32_10_STK"]/div/div/div[1]/label'):
        click_element('xpath=//*[@id="P2000_32_10_STK"]/div/div/div[1]/label')

    if is_element_visible('id=P2000_32_10_RGP'):
        set_registarsko_područje(offer_data.reg_prefix)

    time.sleep(5)
    # Close all messages that might appear and obstruct other elements
    close_all()

    # Wait for the "Izracun" button to appear and click on it
    wait_and_click('id=btnIzracun')

    return df, False



# Step 5: Show the calculated premium and available discounts
def show_premium(df, offer_data):
    """Show the calculated premium and available discounts"""
    #Un-click whatever is clicked within "Rideri AO" container
    browser.wait_until_element_is_visible('xpath=//*[@id="R262954840126205447"]', timeout=60)
    checked_elements = browser.find_elements('xpath=//*[@id="R262954840126205447"]//*[contains(@class, "mdl-switch-item__checked")]')

    for element in checked_elements:
        time.sleep(5)
        click_element(element)

    insurance_premium_xpath = 'xpath=//*[@id="report_reg_izracun_ao"]/tbody/tr[1]/td[2]'
    browser.wait_until_element_is_visible(insurance_premium_xpath, timeout=60)
    #print(browser.get_element_attribute(insurance_premium_xpath, "textContent"))
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
    multiplier = bonus_multipliers.get(str(offer_data.bonus))

    # Calculate the insurance premium if the bonus is valid
    if multiplier is not None:
        insurance_premium = float(element) * multiplier
        #print(insurance_premium)
    else:
        df["Status"] = "Automatski izračun nije moguć. Molim ručni izračun."
        return df, True


    if is_element_visible('id:kom_pop'):
        # Retrieve all options from the dropdown as WebElement objects
        options_1 = Select(browser.find_element('id:kom_pop')).options
        # Get the last option's value
        commercial_discount = float(options_1[-1].get_attribute('value'))
    else:
        commercial_discount = "Nema raspoloživog popusta"

    if is_element_visible('id:pop_savjetnika'):
        #repeat the same for the second dropdown
        options_2 = Select(browser.find_element('id:pop_savjetnika')).options
        advisor_discount = float(options_2[-1].get_attribute('value'))
    else:
        advisor_discount = "Nema raspoloživog popusta"

    # Update the DataFrame
    df['InsurancePremium'] = insurance_premium
    df['CommercialDiscount'] = commercial_discount
    df['AdvisorDiscount'] = advisor_discount
    df['Status'] = "OK"

    return df, False
