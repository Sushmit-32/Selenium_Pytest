from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
button=driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button')
button.click()
time.sleep(3)
a=driver.switch_to.alert

print(a.text)
a.accept()
driver.switch_to.default_content()
options=webdriver.ChromeOptions()
options.headless=True
