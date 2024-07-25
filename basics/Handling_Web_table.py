from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose")
driver.maximize_window()
driver.implicitly_wait(30)

#Single column

sc = driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[6]/td[3]").text
print(sc)

#single row
sr = driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[6]").text
print(sr)

#Entire table
wb_list = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr")
print(len(wb_list))

for i in wb_list:
    print(i.text)