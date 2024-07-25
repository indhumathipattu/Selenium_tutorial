from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
year_dd = driver.find_element(By.ID,"year")
sel = Select(year_dd)
ylist = sel.options
print(len(ylist))
for i in ylist:
    print(i.text)