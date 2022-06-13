"""
here we will use setup and teardown method so that we need not have to use browser invocation code again and again
instead we will create setup_module and teardown_module so that once we initialize that in our code we just have to focus on test case

use following command to generate report "py.test '.\setup mthd.py' --html=test_google.html"

"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver= None
def setup_module():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.google.com")

def teardown_module():
    driver.quit()

def test_demo1():
    print(driver.title)

