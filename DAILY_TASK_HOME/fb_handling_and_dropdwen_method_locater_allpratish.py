import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from basics.Dropdown_handling import Sel

OPT = Options()
OPT.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=OPT)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT, "Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("muthumathi")
driver.find_element(By.NAME, "reg_email__").send_keys("murugan1236@gmail.com")
driver.find_element(By.NAME, "reg_passwd__").send_keys("muruga1")
month_dd = driver.find_element(By.ID, "month")
sel = Select(month_dd)
Sel.select_by_visible_text("Jan")
sel.select_by_value("5")
