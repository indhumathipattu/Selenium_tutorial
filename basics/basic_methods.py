from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.fb.com")
driver.maximize_window()
actual_title = driver.title
print(actual_title)
actual_url = driver.current_url
print(actual_url)
