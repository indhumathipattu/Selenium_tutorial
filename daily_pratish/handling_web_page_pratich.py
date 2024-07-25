from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from basics.Handling_Web_table import wb_list

opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose")
driver.maximize_window()
driver.implicitly_wait(30)
#SINGLE.COLUM
SC=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[6]/td[3]").text
print(SC)
#SINGLE ROW
SC=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[6]").text
print(SC)
#ENTER TABLE
web_list=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr").text
print(len(web_list))
for i in wb_list:
    print(i.text)




