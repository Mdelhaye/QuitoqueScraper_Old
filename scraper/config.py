import os

BASE_URL        = 'https://www.quitoque.fr/recette/'
START_INDEX     = 10000
NB_RECIPES      = 10
MAX_WORKERS     = 10
WEBDRIVER_PATH  = r'./msedgedriver.exe'
OUTPUT_DIR	= r'./PDF'

COOKIE_POPUP_CLOSE_BUTTON_ID	= "onetrust-close-btn-container"

RECIPE_UNVAILABLE_XPATH			= '//h1[text()="Cette recette est introuvable"]'
HELP_CATEGORY_XPATH				= '//h3[text()="Besoin d\'un coup de main ?"]'
HEADER_AND_FOOTER_XPATH			= '/html/body/div/div/*'
BACK_TO_MENU_BUTTON_XPATH		= '//button[text()="Revenir au menu"]'
VIEW_DETAILS_BUTTON_XPATH		= '//button[text()="Voir le détail"]' 
ADD_PERSONN_BUTTON_XPATH		= '//h3[text()=\"personnes\"]/../button[2]'


HEADER_AND_FOOTER_OLD_VERSION_INDICES	= [0, 4, 5, 6]
HEADER_AND_FOOTER_NEW_VERSION_INDICES	= [0, 3, 5, 6, 7, 8]
BACK_TO_MENU_BUTTON_INDICES				= [0]
VIEW_DETAILS_BUTTON_INDICES				= [0, 1]

if not os.path.exists(WEBDRIVER_PATH):
    raise FileNotFoundError(f'WebDriver doesn\'t exists in : {WEBDRIVER_PATH}')

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)