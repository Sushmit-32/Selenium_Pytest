

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.freshworks.com")
wait= WebDriverWait(driver, 10)
a= wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'ul.footer-nav li')))
print(len(a))
for ele in a:
    print(ele.text)