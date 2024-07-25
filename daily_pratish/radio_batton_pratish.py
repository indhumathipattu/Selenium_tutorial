from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from basics.Radio_button import female_radiobtn

opt=Options()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()

#female_ratio_btn=driver.find_element(By.XPATH,"//input[class='_8esa'][@value='1']")
female_radio_btn=driver.find_element(By.NAME,"sex")
#display
ratio2_but=female_radio_btn.is_displayed()
print("female button display=",ratio2_but)
#enable btn
ratio1_enable=female_radio_btn.is_enabled()
print("female ration button enable=",ratio1_enable)
#select button
ratio_btn= female_radio_btn .is_selected()
print("famale ratio button select=",ratio_btn)
female_radio_btn.click()
ratio_btn= female_radio_btn .is_selected()
print("After clicking female radio button select =",ratio_btn)