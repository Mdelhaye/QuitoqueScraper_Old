import os

PDF_DIR_PATH = './../PDF'
LOG_DIR_PATH = './../LOG'

def delete_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

def main():
	if os.path.exists(PDF_DIR_PATH):
		delete_files_in_directory(PDF_DIR_PATH)
	
	if os.path.exists(LOG_DIR_PATH):
		delete_files_in_directory(LOG_DIR_PATH)
		
if __name__ == "__main__":
	main()