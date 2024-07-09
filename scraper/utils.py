from selenium.webdriver.common.by   import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
from selenium.common.exceptions     import TimeoutException

from scraper.config import COOKIE_POPUP_CLOSE_BUTTON_ID, OUTPUT_DIR

import base64
from PIL import Image
import io
import os
import fitz

def handle_cookie_popup(driver, timeout = 1.5):
    """ Handles the cookie popup by clicking the close button. """
    try:
        cookie_popup = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, COOKIE_POPUP_CLOSE_BUTTON_ID))
        )
        cookie_popup.click()
    except TimeoutException:
        pass

def print_to_pdf(driver):
    result = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
    with open(OUTPUT_DIR + f'/{driver.title}.pdf', 'wb') as file:
        file.write(base64.b64decode(result['data']))
    
def extract_images_from_pdf(pdf_path):
    # Ouvrir le fichier PDF
    document = fitz.open(pdf_path)
    images = []

    # Parcourir toutes les pages du document
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))

            images.append((page_num, img_index, image_ext, image))

    return images

def pdf_is_correct(images):
    return True if len(images) == 1 else False

def pdf_exist(title):
    return os.path.exists(OUTPUT_DIR + f'/{title}.pdf')
        