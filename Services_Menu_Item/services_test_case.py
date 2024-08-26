from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, random, string
from General_Navigation import setup_and_navigate_to_website
from Services_Menu_Item import services_web_elements


class AgileBridgeServicesBase:

    def __init__(self, driver):
        self.driver = driver

    def agile_bridge_services_base(self):
        web_elements = services_web_elements.ServicesElements(self.driver)

        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(web_elements.services_menu_item()))
        web_elements.services_menu_item().click()
        WebDriverWait(self.driver, 100).until(EC.url_contains("services"))
        current_url = self.driver.current_url
        if "services" in current_url:
            print("Successfully navigated to the expected page.")
        else:
            print("Navigation to the expected page failed.")

        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(web_elements.button_lets_connect_top_right()))
        web_elements.button_lets_connect_top_right().click()
        WebDriverWait(self.driver, 100).until(EC.url_contains("contact-us"))
        current_url_1 = self.driver.current_url
        if "contact-us" in current_url_1:
            print("Successfully navigated to the expected page.")
        else:
            print("Navigation to the expected page failed.")
        self.driver.back()

        time.sleep(5)

        return self.driver

class AgileBridgeServices(unittest.TestCase):

    def setUp(self):
        self.driver = None
        setup_and_navigate_instance = setup_and_navigate_to_website.SetupAndNavigate()
        self.driver = setup_and_navigate_instance.setup_and_navigate()

    def test_agile_bridge_services(self):
        services_instance = AgileBridgeServicesBase(self.driver)
        self.driver = services_instance.agile_bridge_services_base()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
