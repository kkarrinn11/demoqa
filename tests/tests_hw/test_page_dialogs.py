from pages.modal_dialogs import ModalDialogs
from components.components import WebElement

def test_modal_elements(browser):
    modal = ModalDialogs (browser)
    modal.visit ()
    assert modal.not_uni.check_count_elements(count=5)



def test_navigation_modal(browser):
    navigation = ModalDialogs (browser)
    navigation.visit()
    navigation.refresh()
    navigation.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    navigation.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)