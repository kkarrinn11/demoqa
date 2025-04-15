from pages.webtables import Tables
import time

def test_tables (browser):
    page_tables = Tables(browser)

    page_tables.visit()
    assert page_tables.btn_add.exist()
    page_tables.btn_add.click()
    assert not page_tables.btn_submit.click()
    page_tables.first_name.send_keys('Slava')
    page_tables.last_name.send_keys('Ivanov')
    page_tables.user_email.send_keys('slava.ivanov@mail.ru')
    page_tables.age.send_keys('13')
    page_tables.salary.send_keys('200')
    page_tables.department.send_keys('UCR')
    page_tables.btn_submit.click()
    assert page_tables.table_name.get_text() == 'Slava'
    page_tables.edit.click()
    page_tables.first_name.clear()
    page_tables.first_name.send_keys('Max')
    page_tables.btn_submit.click()
    assert page_tables.table_name.get_text() == 'Max'
    page_tables.btn_delete_row_new.click()
    assert page_tables.table_name.get_text() == ' '

