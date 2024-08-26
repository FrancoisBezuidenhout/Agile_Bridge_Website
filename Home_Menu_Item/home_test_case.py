from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, random, string
from General_Navigation import setup_and_navigate_to_website
from Home_Menu_Item import home_web_elements


class AgileBridgeHomeBase:

    def __init__(self, driver):
        self.driver = driver

    def agile_bridge_home_base(self):
        web_elements = home_web_elements.HomeElements(self.driver)

        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(web_elements.home_menu_item()))
        web_elements.home_menu_item().click()

        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(web_elements.button_lets_connect_top_right()))
        web_elements.button_lets_connect_top_right().click()
        WebDriverWait(self.driver, 100).until(EC.url_matches("https://agilesandbox.co.za/contact-us/"))
        current_url_1 = self.driver.current_url
        if "https://agilesandbox.co.za/contact-us/" in current_url_1:
            print("Successfully navigated to the expected page.")
        else:
            print("Navigation to the expected page failed.")
        self.driver.back()

        time.sleep(2)
        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(web_elements.button_lets_connect_middle()))
        web_elements.button_lets_connect_middle().click()
        WebDriverWait(self.driver, 100).until(EC.url_contains("contact-us"))
        current_url_2 = self.driver.current_url
        if "contact-us" in current_url_2:
            print("Successfully navigated to the expected page.")
        else:
            print("Navigation to the expected page failed.")
        self.driver.back()

        time.sleep(2)
        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(web_elements.button_learn_more()))
        web_elements.button_learn_more().click()
        WebDriverWait(self.driver, 100).until(EC.url_contains("our-company"))
        current_url_3 = self.driver.current_url
        if "our-company" in current_url_3:
            print("Successfully navigated to the expected page.")
        else:
            print("Navigation to the expected page failed.")
        self.driver.back()

        time.sleep(2)
        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(web_elements.button_our_services()))
        web_elements.button_our_services().click()
        WebDriverWait(self.driver, 100).until(EC.url_contains("services"))
        current_url_4 = self.driver.current_url
        if "services" in current_url_4:
            print("Successfully navigated to the expected page.")
        else:
            print("Navigation to the expected page failed.")
        self.driver.back()

        time.sleep(2)
        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(web_elements.button_lets_chat()))
        web_elements.button_lets_chat().click()
        WebDriverWait(self.driver, 100).until(EC.url_contains("contact-us"))
        current_url_5 = self.driver.current_url
        if "contact-us" in current_url_5:
            print("Successfully navigated to the expected page.")
        else:
            print("Navigation to the expected page failed.")
        self.driver.back()

        time.sleep(5)

        return self.driver

class AgileBridgeHome(unittest.TestCase):

    def setUp(self):
        self.driver = None
        setup_and_navigate_instance = setup_and_navigate_to_website.SetupAndNavigate()
        self.driver = setup_and_navigate_instance.setup_and_navigate()

    def test_agile_bridge_home(self):
        home_instance = AgileBridgeHomeBase(self.driver)
        self.driver = home_instance.agile_bridge_home_base()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
