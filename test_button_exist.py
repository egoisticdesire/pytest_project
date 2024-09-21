import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_button_exist(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    assert driver.find_element(By.ID, 'submit-id-submit').is_displayed()
