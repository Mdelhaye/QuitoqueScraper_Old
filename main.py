from cleaner.clean_folder import main as cleanerMain

import re

def main():
    # End of scrapping message
    print("Scrapping ended.")

# Script entry point
if __name__ == "__main__":
	print("MAIN MENU".center(80, "-"))
	print("1. Scraper\n2. Cleaner")

	selection = 0
	while int(selection) != 1 and int(selection) != 2:
		selection = input("--> Choose between the options (default Scraper): ")
		selection = selection if re.match(r'^(\d)$', selection) else 1

	if int(selection) == 2:
		cleanerMain()	# Calls the Main function of clean_folder.py if the option selected is "2"
	elif int(selection) == 1:
	 	main()	# Calls the Main function if the option selected is "1" or wrong
