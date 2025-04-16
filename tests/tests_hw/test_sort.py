from pages.webtables import Tables


def test_sort (browser):
    sort = Tables (browser)
    sort.visit()

    sort.f_name.click()
    assert sort.f_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    sort.l_name.click()
    assert sort.l_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    sort.age_tab.click()
    assert sort.age_tab.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    sort.salary_tab.click()
    assert sort.salary_tab.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    sort.email.click()
    assert sort.email.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    sort.department_tab.click()
    assert sort.department_tab.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    sort.action.click()
    assert sort.action.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
