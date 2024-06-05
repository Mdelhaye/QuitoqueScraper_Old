import os

ADD_PERSONS_SCRIPT		= ""
ADD_PERSONS_SCRIPT_PATH	= r"./scraper/scripts/addPersons.js"

CHECK_RECIPE_AVAILABILITY_SCRIPT 	  = ""
CHECK_RECIPE_AVAILABILITY_SCRIPT_PATH = r"./scraper/scripts/checkAvailability.js"

MANIPULATE_ELEMENTS_SCRIPT		= ""
MANIPULATE_ELEMENTS_SCRIPT_PATH	= r"./scraper/scripts/manipulateElements.js"

if os.path.exists(ADD_PERSONS_SCRIPT_PATH):
	with open(ADD_PERSONS_SCRIPT_PATH, "r") as js_file:
		ADD_PERSONS_SCRIPT = js_file.read()
	
if os.path.exists(CHECK_RECIPE_AVAILABILITY_SCRIPT_PATH):
	with open(CHECK_RECIPE_AVAILABILITY_SCRIPT_PATH, "r") as js_file:
		CHECK_RECIPE_AVAILABILITY_SCRIPT = js_file.read()
		
if os.path.exists(MANIPULATE_ELEMENTS_SCRIPT_PATH):
	with open(MANIPULATE_ELEMENTS_SCRIPT_PATH, "r") as js_file:
		MANIPULATE_ELEMENTS_SCRIPT = js_file.read()