import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.fb.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy _9npi']").send_keys("meena@12")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Indu123")
acutul_title=driver.title
print(acutul_title)
acutul_url=driver.current_url
print(acutul_url)
time.sleep(5)

#x path la url and tittle printe pratish