from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.co.in/")
print(driver.title)
