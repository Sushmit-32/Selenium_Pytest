from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.spicejet.com/')
time.sleep(3)
loc_ele = driver.find_element(By.XPATH,'//div[@class=css-1dbjc4n r-1awozwy r-1loqt21 r-18u37iz r-le9fof r-1otgn73]/div[@class=css-1dbjc4n r-1awozwy r-1loqt21 r-18u37iz r-le9fof r-1otgn73]')
action = ActionChains(driver)
action.move_to_element(loc_ele).perform()
