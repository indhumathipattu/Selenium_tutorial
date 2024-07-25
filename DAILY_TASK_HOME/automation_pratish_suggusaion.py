from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.ID,"autocomplete")
lis_li=driver.find_elements(By.ID,"ui-id-48")
print(len(lis_li))