from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.rediff.com/")
driver.maximize_window()
link_li = driver.find_elements(By.TAG_NAME, "a")
print(len(link_li))

for i in link_li:
    print(i.text, "--->",i.get_attribute("href"))