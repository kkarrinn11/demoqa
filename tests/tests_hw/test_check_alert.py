import time

from pages.alerts import Alerts


def test_check_alert (browser):
    alert = Alerts (browser)

    alert.visit()
    alert.timerButton.click()
    time.sleep(6)
    assert alert.alert()
