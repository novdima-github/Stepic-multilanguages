import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_exist(browser):
    browser.get(link)
    time.sleep(5)
    add_to_cart_button = WebDriverWait(browser, 5).\
        until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
    assert add_to_cart_button, "No 'Add to basket button exist'..."
