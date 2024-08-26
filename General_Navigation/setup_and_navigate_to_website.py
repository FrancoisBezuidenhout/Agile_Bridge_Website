# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class SetupAndNavigate:

    def __init__(self):
        self.driver = None

    def setup_and_navigate(self, options=None):

        chrome_driver_path = 'C:\\Users\\LANSOLO\\AquaProjects\\Agile_Bridge_Website\\drivers\\chromedriver.exe'

        service = Service(executable_path=chrome_driver_path)

        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(120)
        self.driver.maximize_window()
        self.driver.get("https://www2.agilebridge.co.za/")

        return self.driver


if __name__ == "__main__":
    setup_and_navigate_instance = SetupAndNavigate()
    setup_and_navigate_instance.setup_and_navigate()
