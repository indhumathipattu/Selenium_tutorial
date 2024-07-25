from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.rediff.com/")
driver.maximize_window()
driver.implicitly_wait(35)
list_text=driver.find_elements(By.TAG_NAME,"iframe")
print(len(list_text))
for i in list_text:
    print(i.text)