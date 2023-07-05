class Page:
    def __init__(self,url):
        self.url = url

    def get(self):
        print(self.url)
home = Page('http://84.204.33.180:5004/sp/')
home.get()

