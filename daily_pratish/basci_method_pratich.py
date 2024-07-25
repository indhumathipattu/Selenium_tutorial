import time
from tkinter.tix import Select

from select import select
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
alt_text=driver.find_element(By.NAME,"email").get_attribute("placeholder")
print(alt_text)
text1=driver.page_source
print(text1)
text3 = driver.find_element(By.ID,"email").value_of_css_property("color")
print(text3)

#text2=driver.find_element(By.ID,"emila").value_of_css_property("color")
#print(text2)
text3=driver.find_element(By.ID,"email").value_of_css_property("hight")
print(text3)
text4=driver.find_element(By.ID,"email").value_of_css_property("weight")
print(text4)
text5=driver.find_element(By.ID,"email").value_of_css_property("font_size")
print(text5)
driver.find_element(By.ID,"email").send_keys("indhumathi")
driver.find_element(By.NAME,"pass").send_keys("indhu@123")
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("Indhumathi")
driver.find_element(By.NAME,"reg_email__").send_keys("mathiindu13@gmail.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys("meena@12")
mm_t1=driver.find_element(By.ID,"day")
day=driver.find_element(By.ID,"month")
year_t2=driver.find_element(By.NAME,"birthday_year")
driver.find_element(By.NAME,"sex").click()
#driver.find_element(By.CLASS_NAME,"hidden_elem _58ml").click()
#day
dd_text2=Select(mm_t1)
dd_text2.select_by_visable_text("22")
time.sleep(5)
dd_text2.select_by_value("19")
#month
month_text1=Select(day)
month_text1.select_by_visable_text("Aug")
month_text1.select_by_value("8")
month_text1.select_by_index(9)
time.sleep(5)
#year
year_text=Select(year_t2)
year_text.select_by_visable_text("2020")
time.sleep(5)
year_text.select_by_value("2020")
