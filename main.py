from cleaner.clean_folder 	import main as cleanerMain
from scraper.scraper		import scrape_urls
from scraper.config			import BASE_URL, START_INDEX, NB_RECIPES, WEBDRIVER_PATH

import re
import time

def main():
	GLOBAL_START_TIME = time.time()

	urls = [f'{BASE_URL}{i}' for i in range(START_INDEX, START_INDEX + NB_RECIPES)]
	results = scrape_urls(urls, WEBDRIVER_PATH)

	GLOBAL_ENDED_TIME = time.time()

	for result in results:
		print(result)

    # End of scrapping message
	print(f"Scrapping ended. {GLOBAL_ENDED_TIME - GLOBAL_START_TIME}")

# Script entry point
if __name__ == "__main__":
	print("MAIN MENU".center(80, "-"))
	print("1. Scraper\n2. Cleaner")

	selection = 0
	while int(selection) != 1 and int(selection) != 2:
		selection = input("--> Choose between the options (default 1): ")
		selection = selection if re.match(r'^(\d)$', selection) else 1

	if int(selection) == 2:
		print('\nCalling cleaning method.\n')
		cleanerMain()	# Calls the Main function of clean_folder.py if the option selected is "2"
	elif int(selection) == 1:
		print('\nCalling scrapping method.\n')
		main()  # Calls the Main function if the option selected is "1" or wrong
