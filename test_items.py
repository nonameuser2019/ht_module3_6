import pytest
from selenium import webdriver
import time

def test_check_item_add_to_bag(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    button_add_bug = browser.find_element_by_class_name('btn.btn-lg.btn-primary.btn-add-to-basket')
    button_add_bug.click()
    time.sleep(30)
    assert True