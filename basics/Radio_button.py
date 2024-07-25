import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#isSelected, isDisplayed, isEnabled

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()

female_radiobtn = driver.find_element(By.XPATH,"//input[@class='_8esa'][@value='1']")

#female radio btn display

radio1_display =female_radiobtn.is_displayed()
print("Female radio button display = ", radio1_display)

#female radio btn enable
radio1_enable = female_radiobtn.is_enabled()
print("Female radio button enable = ", radio1_enable)

#female radio btn selecte
radio1_select = female_radiobtn.is_selected()
print("Female radio button select = ", radio1_select)

#Female radio btn click
female_radiobtn.click()

#female radio btn selecte
radio1_select1 = female_radiobtn.is_selected()
print("After clicking female radio button select = ", radio1_select1)