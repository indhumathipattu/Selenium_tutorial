import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome()
driver.get("http://www.FB.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.PARTIAL_LINK_TEXT," new account").click()
driver.find_element(By.NAME,"firstname").send_keys("indhumathi")
time.sleep(5)
act =ActionChains(driver)
act.send_keys(Keys.TAB).send_keys("M").send_keys(Keys.TAB).send_keys("indhumathi1223@gmail.com").send_keys(Keys.TAB).send_keys("indhumathi1223@gmail.com").perform()
