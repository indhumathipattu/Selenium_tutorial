import time

from selenium import webdriver

driver = webdriver.ChromiumEdge()
driver.get('http://www.facebook.com')
driver.maximize_window()
time.sleep(5)
actural_tittle = driver.tittle
print('acturl_tittle')
actural_url = driver.current_url
print("actulal url")
#==================================
print("========================================")

driver = webdriver.Firefox()
driver.get("http://www.amezon.com")
driver.maximize_window()
actural_tittle=driver.title
print(actural_tittle)
actural_url=driver.current_url
print(actural_url)
