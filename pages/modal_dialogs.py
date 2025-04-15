from components.components import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ModalDialogs (BasePage):

    def __init__(self, driver, locator = ''):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        self.locator = locator
        self.icon = WebElement(driver, '#app > header > a')
        super().__init__(driver, self.base_url)

        self.not_uni = WebElement (driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count: int) -> bool:
            if len(self.find_elements()) == count:
                return True
            return False


