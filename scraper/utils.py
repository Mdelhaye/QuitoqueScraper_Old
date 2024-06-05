from selenium.webdriver.common.by   import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
from selenium.common.exceptions     import TimeoutException

from scraper.config import COOKIE_POPUP_CLOSE_BUTTON_ID

def handle_cookie_popup(driver, timeout = 1.5):
    """ Handles the cookie popup by clicking the close button. """
    try:
        cookie_popup = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, COOKIE_POPUP_CLOSE_BUTTON_ID))
        )
        cookie_popup.click()
    except TimeoutException:
        pass