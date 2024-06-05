from selenium                           import webdriver                # Importing the Selenium WebDriver module
from selenium.webdriver.edge.service    import Service as EdgeService   # Importing the service for Microsoft Edge
from selenium.webdriver.edge.options    import Options                  # Importing options for Microsoft Edge

from scraper.utils  import handle_cookie_popup
from scraper.config import (RECIPE_UNVAILABLE_XPATH, HELP_CATEGORY_XPATH,
							HEADER_AND_FOOTER_XPATH, HEADER_AND_FOOTER_OLD_VERSION_INDICES, HEADER_AND_FOOTER_NEW_VERSION_INDICES,
							BACK_TO_MENU_BUTTON_XPATH, BACK_TO_MENU_BUTTON_INDICES,
							VIEW_DETAILS_BUTTON_XPATH, VIEW_DETAILS_BUTTON_INDICES,
                            ADD_PERSONN_BUTTON_XPATH)

from scraper.script import CHECK_RECIPE_AVAILABILITY_SCRIPT, MANIPULATE_ELEMENTS_SCRIPT, ADD_PERSONS_SCRIPT

def initialize_browser(webdriver_path):
    """ Initializes the Edge WebDriver with the specified options. """
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument("--disable-popup-blocking")
    edge_options.set_capability(
        "ms:loggingPrefs", {"browser": "OFF", "driver": "SEVERE", "performance": "OFF"}
    )

    service = EdgeService(webdriver_path)
    return webdriver.Edge(service=service, options=edge_options)

def scrape_website(url, webdriver_path, max_retry = 0):
    """ Scrapes the website at the given URL using the specified WebDriver path. """
    try:
        driver = initialize_browser(webdriver_path)
        driver.get(url)

        handle_cookie_popup(driver)

        recipe_unvailable_result = driver.execute_script(CHECK_RECIPE_AVAILABILITY_SCRIPT + " return checkAvailability(" + str([f"{RECIPE_UNVAILABLE_XPATH}", f"{HELP_CATEGORY_XPATH}"]) + ");")
        if recipe_unvailable_result['success'] == False:
            return recipe_unvailable_result['message']
        
        HEADER_AND_FOOTER_INDICES = HEADER_AND_FOOTER_NEW_VERSION_INDICES if recipe_unvailable_result['success'] == False and recipe_unvailable_result['message'] == 'Help category available!' else HEADER_AND_FOOTER_OLD_VERSION_INDICES

        global_result = driver.execute_script(MANIPULATE_ELEMENTS_SCRIPT + " return manipulateElements(" + str([f"{HEADER_AND_FOOTER_XPATH}", f"{BACK_TO_MENU_BUTTON_XPATH}"]) + ", " + str([f"{HEADER_AND_FOOTER_INDICES}", f"{BACK_TO_MENU_BUTTON_INDICES}"]) + ", " + str([f"{VIEW_DETAILS_BUTTON_XPATH}"]) + ", " + str([f"{VIEW_DETAILS_BUTTON_INDICES}"]) + ");")
        if global_result['success'] == False:
            return global_result['message']
        
        add_personn_result = driver.execute_script(ADD_PERSONS_SCRIPT + " return addPersons('" + ADD_PERSONN_BUTTON_XPATH + "')")
        if add_personn_result['success'] == False:
            return add_personn_result['message']
        
    except Exception as e:
        print("ERROR".center(80,'-'))
        print(e)
        
    finally:
        driver.quit()