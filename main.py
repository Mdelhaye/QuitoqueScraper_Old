from cleaner.clean_folder 	import main as cleanerMain
from scraper.scraper		import scrape_urls

import re
import time
import pprint

def main():
	GLOBAL_START_TIME = time.time()

	urls = [f'https://www.quitoque.fr/recette/{i}' for i in range(10000, 10000 + 10)]
	pprint.pprint(scrape_urls(urls, r'./msedgedriver.exe'))

	GLOBAL_ENDED_TIME = time.time()

    # End of scrapping message
	print(f"Scrapping ended. {GLOBAL_ENDED_TIME - GLOBAL_START_TIME}")

# Script entry point
if __name__ == "__main__":
	print("MAIN MENU".center(80, "-"))
	print("1. Scraper\n2. Cleaner")

	selection = 0
	while int(selection) != 1 and int(selection) != 2:
		selection = input("--> Choose between the options (default Scraper): ")
		selection = selection if re.match(r'^(\d)$', selection) else 1

	if int(selection) == 2:
		print('\nCalling cleaning method.\n')
		cleanerMain()	# Calls the Main function of clean_folder.py if the option selected is "2"
	elif int(selection) == 1:
		print('\nCalling scrapping method.\n')
		main()  # Calls the Main function if the option selected is "1" or wrong
