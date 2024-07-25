from optparse import Option

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt =Options()
opt.and_expirimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
driver.find_element(By.XPATH,"html/body/center/form/div/table[2]/tbody/tr[3]/td[3]/input").send_keys("Indhumathi")
driver.implicitly_wait(30)
driver.find_element(By.NAME,"login35c9a71").send_keys("@rediffmail.com")

