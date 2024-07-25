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
day_dd = driver.find_element(By.ID,"day")
sel = Select(day_dd)
dlist = sel.options
for d in dlist:
    print(d.text)

#taking all values from dd3 month task in fb
#pratish for rediff .com for all method basi.