from RPA.Browser.Selenium import Selenium

# Create a Selenium instance and assign it to a variable
browser = Selenium()

def click_element(locator):
    """Clicks on an element"""
    browser.click_element(locator)

def input_text(locator, text):
    """Inputs text into an element"""
    browser.input_text(locator, text)

def wait_and_click(locator):
    """Waits for an element to appear and then clicks on it"""
    browser.wait_until_element_is_visible(locator, timeout=90)
    browser.click_element(locator)

def wait_and_input_text(locator, text):
    """Waits for an element to appear and then inputs text into it"""
    browser.wait_until_element_is_visible(locator, timeout=90)
    browser.input_text(locator, text)

def get_text_xpath(text):
    """Returns an xpath that contains a certain text attribute"""
    return f'xpath=//*[contains(text(), "{text}")]'

def is_element_visible(locator):
    """Returns True if an element is visible, otherwise returns False"""
    return browser.is_element_visible(locator)

def is_element_visible_by_text_attribute(text):
    """Returns True if an element is visible, otherwise returns False"""
    return browser.is_element_visible(get_text_xpath(text))

def close_all():
    """Closes all toaster messages that might appear"""
    if is_element_visible(get_text_xpath("zatvori sve")):
        browser.click_element(get_text_xpath("zatvori sve"))

def open_browser(url):
    """Opens the browser"""
    browser.auto_close = False
    browser.open_available_browser(url, maximized=True)

def close_browser():
    """Closes the browser"""
    browser.close_browser()
