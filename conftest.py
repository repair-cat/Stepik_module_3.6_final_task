import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    print(f"\nopen site with {language} language..")
    browser = webdriver.Chrome()
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/' 
    browser.get(link)   
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()