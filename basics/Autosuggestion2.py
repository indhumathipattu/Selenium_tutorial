import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.ID,"APjFqb").send_keys("Selenium")
list_opt = driver.find_elements(By.XPATH,"//div[@class='erkvQe']/div/ul/li")
print(len(list_opt))
time.sleep(5)

for i in list_opt:

    if i.text == "selenium webdriver":
        i.click()
        break
