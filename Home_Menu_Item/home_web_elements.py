from selenium.webdriver.common.by import By
from selenium import webdriver


class HomeElements:
    def __init__(self,driver=None):

        self.driver = driver if driver else webdriver.Chrome()
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # Menu_Item
    def home_menu_item(self):
        return self.driver.find_element(By.XPATH, "//a[@class='hfe-menu-item'][contains(text(),'Home')]")

    # Home Page buttons
    def button_learn_more(self):
        return self.driver.find_element(By.XPATH, "//span[@class='elementor-button-text'][contains(text(),'Learn More')]")

    def button_lets_connect_top_right(self):
        return self.driver.find_element(By.XPATH, "//div[@class='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-a8acb85 nav-button']//a[@class='elementor-button elementor-button-link elementor-size-sm']//span[@class='elementor-button-text'][contains(text(),\"Let's Connect\")]")

    def button_lets_connect_middle(self):
        return self.driver.find_element(By.XPATH, "//div[@data-id='8a80e94']//a[@class='elementor-button elementor-button-link elementor-size-sm']//span[@class='elementor-button-text'][contains(text(),\"Let's Connect\")]")


    def button_our_services(self):
        return self.driver.find_element(By.XPATH, "//span[@class='elementor-button-text'][contains(text(),'Our Services')]")

    def button_lets_chat(self):
        return self.driver.find_element(By.XPATH, "//span[@class='elementor-button-text'][contains(text(),\"Let's Chat\")]")
