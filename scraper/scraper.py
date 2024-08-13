import concurrent.futures 
import os

from selenium                           import webdriver                # Importing the Selenium WebDriver module
from selenium.webdriver.edge.service    import Service as EdgeService   # Importing the service for Microsoft Edge
from selenium.webdriver.edge.options    import Options                  # Importing options for Microsoft Edge

from scraper.utils  import handle_cookie_popup, print_to_pdf, extract_images_from_pdf, pdf_is_correct, pdf_exist
from scraper.config import (RECIPE_UNVAILABLE_XPATH, HELP_CATEGORY_XPATH,
							HEADER_AND_FOOTER_XPATH, HEADER_AND_FOOTER_OLD_VERSION_INDICES, HEADER_AND_FOOTER_NEW_VERSION_INDICES,
							BACK_TO_MENU_BUTTON_XPATH, BACK_TO_MENU_BUTTON_INDICES,
							VIEW_DETAILS_BUTTON_XPATH, VIEW_DETAILS_BUTTON_INDICES,
                            ADD_PERSONN_BUTTON_XPATH, OUTPUT_DIR, MAX_WORKERS, WEBDRIVER_PATH)

from scraper.script import CHECK_RECIPE_AVAILABILITY_SCRIPT, MANIPULATE_ELEMENTS_SCRIPT, ADD_PERSONS_SCRIPT

from scraper.custom_objects import ScrapingResult
from scraper.custom_exceptions import WebDriverNotFoundError, PDFGenerationError, ScrapingError

def initialize_browser(webdriver_path):
    """ Initializes the Edge WebDriver with the specified options. """
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument("--disable-popup-blocking")
    edge_options.set_capability(
        "ms:loggingPrefs", {"browser": "OFF", "driver": "SEVERE", "performance": "OFF"}
    )
    
    if not os.path.exists(WEBDRIVER_PATH):
        raise WebDriverNotFoundError(f'WebDriver not found at path: {WEBDRIVER_PATH}')

    service = EdgeService(webdriver_path)

    return webdriver.Edge(service=service, options=edge_options)

def scrape_website(url, webdriver_path, max_retry = 0):
    """ Scrapes the website at the given URL using the specified WebDriver path. """
    result = ScrapingResult(url)
    driver = None
    try:
        driver = initialize_browser(webdriver_path)
        driver.get(url)

        if pdf_exist(driver.title) and driver.title != 'Quitoque':
            raise ScrapingError(url, 'PDF already exists!')

        handle_cookie_popup(driver)
        
        recipe_unvailable_result = driver.execute_script(CHECK_RECIPE_AVAILABILITY_SCRIPT + " return checkAvailability(" + str([f"{RECIPE_UNVAILABLE_XPATH}", f"{HELP_CATEGORY_XPATH}"]) + ");")
        if recipe_unvailable_result['success'] == False:
            raise ScrapingError(recipe_unvailable_result['message'])
        
        if recipe_unvailable_result['success'] == False and recipe_unvailable_result['message'] == 'Help category available!':
            HEADER_AND_FOOTER_INDICES = HEADER_AND_FOOTER_NEW_VERSION_INDICES
        else:
            HEADER_AND_FOOTER_INDICES = HEADER_AND_FOOTER_OLD_VERSION_INDICES

        global_result = driver.execute_script(MANIPULATE_ELEMENTS_SCRIPT + " return manipulateElements(" + str([f"{HEADER_AND_FOOTER_XPATH}", f"{BACK_TO_MENU_BUTTON_XPATH}"]) + ", " + str([f"{HEADER_AND_FOOTER_INDICES}", f"{BACK_TO_MENU_BUTTON_INDICES}"]) + ", " + str([f"{VIEW_DETAILS_BUTTON_XPATH}"]) + ", " + str([f"{VIEW_DETAILS_BUTTON_INDICES}"]) + ");")
        if global_result['success'] == False:
            raise ScrapingError(global_result['message'])
        
        add_person_result = driver.execute_script(ADD_PERSONS_SCRIPT + " return addPersons('" + ADD_PERSONN_BUTTON_XPATH + "')")
        if add_person_result['success'] == False:
            raise ScrapingError(add_person_result['message'])
        
    except Exception as e:
        result.update(success = False, error = e.__class__.__name__, message = str(e))

    else: 
        if not pdf_exist(driver.title) and driver.title != 'Quitoque':
            print_to_pdf(driver)
            if not pdf_is_correct(extract_images_from_pdf(f'{OUTPUT_DIR}{driver.title}.pdf')):
                raise PDFGenerationError(f'Error generating correct PDF for URL: {url}')
            
        result.update(success = True, message = "Scraping and PDF generation successful")

    finally:
        if driver:
            driver.quit()
    
    return result

def scrape_urls(urls, webdriver_path, max_workers = MAX_WORKERS):
    """ Scrapes multiple URLs concurrently. """
    all_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers = max_workers) as executor:
        futures = [executor.submit(scrape_website, url, webdriver_path) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                all_results.append(result)
            except Exception as e:
                all_results.append(ScrapingResult('', success=False, error=e.__class__.__name__, message=str(e)))

    print(f"Total URLs: {len(urls)}.\nTotal Results: {len(all_results)}.\n")
    return all_results