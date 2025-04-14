from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.element = WebElement(driver, '#section1Content > p')
        self.element_2 = WebElement (driver, '#section1Heading')

        self.element_3 = WebElement (driver, '#section2Content > p:nth-child(1)')
        self.element_4 = WebElement (driver, '#section2Content > p:nth-child(2)')
        self.element_5 = WebElement (driver, '#section3Content > p')