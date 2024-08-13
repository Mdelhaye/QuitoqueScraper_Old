class ScrapingResult:
    def __init__(self, url, success = True, error = None, message = None):
        self.url 		= url
        self.error		= error
        self.success	= success
        self.message 	= message

    def reset(self):
        self.url = ""
        self.success = None
        self.error = None
        self.message = ""

    def update(self, url = None, success = True, error = None, message = None):
        if url is not None:
            self.url = url
        if success is not None:
            self.success = success
        if error is not None:
            self.error = error
        if message is not None:
            self.message = message

    def __str__(self):
        return f"URL: {self.url}, Success: {self.success}, Error: {self.error}, Message: {self.message}"