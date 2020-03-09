import pytest
from selenium import webdriver

def test_find_button_of_basket(browser):
    assert browser.find_element_by_class_name('btn')
