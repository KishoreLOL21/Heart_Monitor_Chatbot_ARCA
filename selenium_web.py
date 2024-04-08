# Web Browsing functionality to the Bot

from selenium import webdriver

class web_search():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    def search_info(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")

search = web_search()
search.search_info("Hello")