import pytest
from selenium import webdriver
from pages.demoqa import DemoQa

@pytest.fixture(scope = 'session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

