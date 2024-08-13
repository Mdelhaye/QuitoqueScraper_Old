class WebDriverNotFoundError(Exception):
	def __init__(self, message = 'WebDriver not found.'):
		self.message = message
		super().__init__(self.message)

class PDFGenerationError(Exception):
	def __init__(self, message = 'Error generating PDF.'):
		self.message = message
		super().__init__(self.message)

class ScrapingError(Exception):
	def __init__(self, message = 'Error scraping URL.'):
		self.message = message
		super().__init__(self.message)