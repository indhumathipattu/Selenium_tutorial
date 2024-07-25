from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.facebook.com/")
driver.maximize_window()
list_lis=driver.find_elements(By.TAG_NAME,'a')
print(len(list_lis))
for i in list_lis:
     print(i.text,'------>',i.get_attribute("herf"))