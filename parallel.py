#do install pytest-xdist before executing in parallel mode

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

a=[]
def test_google():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title=="Google"
    b=driver.title
    a.append(b)
    driver.quit()

def test_yahoo():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.yahoo.com")
    assert driver.title=="yahoo"
    b = driver.title
    a.append(b)
    driver.quit()

def test_facebook():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.facebook.com")
    assert driver.title=="facebook"
    b = driver.title
    a.append(b)
    driver.quit()

print(a)
