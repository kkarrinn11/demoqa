from pages.modal_dialogs import ModalDialogs


def test_check_modal (browser):
    modal = ModalDialogs (browser)
    modal.visit()

    assert modal.btn_small.exist()
    assert modal.btn_large.exist()
    modal.btn_small.click()
    assert modal.btn_close_sm.exist()
    modal.btn_close_sm.click()
    modal.btn_large.click()
    assert modal.btn_close_la.exist()
    modal.btn_close_la.click()