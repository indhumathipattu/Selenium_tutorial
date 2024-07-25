import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

opt= Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
time.sleep(5)
#driver.save_screenshot("C:\\Users\\mathi\\Desktop\\Screenshot\\screenshort4.png")
time.sleep(5)
driver.find_element(By.NAME,"email").send_keys("murugeshwariI123@gmail.com")
driver.find_element(By.ID,"pass").send_keys("indhu1@123")
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//input[@aria-label='First name']").send_keys("Indhumathi")
driver.find_element(By.NAME,"lastname").send_keys("M")
time.sleep(3)
driver.find_element(By.NAME,"reg_email__").send_keys("8963258752")
time.sleep(2)
driver.find_element(By.NAME,"reg_passwd__").send_keys("muthu123")
month_dd3=driver.find_element(By.ID,"month")
sel= Select(month_dd3)
dlist= sel.options
sel.select_by_visible_text("Jan")
print(len(dlist))
for mm in dlist:
    print(mm.text)
year_dd = driver.find_element(By.ID,"year")
sel = Select(year_dd)
ylist = sel.options
sel.select_by_visible_text("2022")
print(len(ylist))
for i in ylist:
    print(i.text)
day_dd = driver.find_element(By.ID,"day")
sel = Select(day_dd)




