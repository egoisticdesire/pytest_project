import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_button_exist(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    assert driver.find_element(By.ID, 'submit-id-submit').is_displayed()


def test_second_button_exist(driver):
    driver.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert driver.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()
