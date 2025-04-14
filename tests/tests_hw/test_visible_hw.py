import time

from pages.accordion import Accordion


def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert accordion.element.visible()

    accordion.element_2.click()
    time.sleep(2)
    assert not accordion.element.visible()


def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert not accordion.element_3.visible()
    assert not accordion.element_4.visible()
    assert not accordion.element_5.visible()