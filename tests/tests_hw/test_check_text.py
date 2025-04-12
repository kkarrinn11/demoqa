from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_text(demoqa_page):
    text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    actual_text = demoqa_page.footer.get_text()
    assert actual_text == text
    demoqa_page.btn_elements.click()

    elements_page = ElementsPage(demoqa_page.driver)

    expected_text = 'Please select an item from left to start practice.'
    actual_text = elements_page.center_text.get_text()

    assert expected_text in actual_text