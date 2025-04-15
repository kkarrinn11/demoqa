from pages.text_box import TextBox


def test_text_box (browser):
    text = TextBox (browser)

    text.visit()
    text.name.send_keys('Karina')
    text.current_address.send_keys('Pushkina str')
    text.btn_submit.click()
    assert text.result_name.get_text() == 'Name:Karina'
    assert text.result_address.get_text() == 'Current Address :Pushkina str'
