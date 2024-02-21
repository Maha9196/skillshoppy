from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import csv
from config.testconfig import TestConfig
from testdata.sklogindata import SKLoginData
class Helper:

    driver=None
    def create_driver(self):
        browser = TestConfig.browser_name
        if browser == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "edge":
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        return self.driver

    def open_url(self):
        self.driver.maximize_window()
        self.driver.get(TestConfig.prod_url)
        time.sleep(5)
        assert self.driver.title == SKLoginData.sk_title

    def close_browser(self):
        time.sleep(3)
        self.driver.quit()

    def getuserlist(self):
        fobj=open("../testdata/userlist.csv", "r")
        userlist=csv.reader(fobj)
        return userlist

    def getregisterlist(self):
        fobj=open("../testdata/registerlist.csv", "r")
        registerlist=csv.reader(fobj)
        return registerlist
