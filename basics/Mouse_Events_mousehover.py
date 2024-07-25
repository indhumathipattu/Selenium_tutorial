import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(5)
comp_ele = driver.find_element(By.XPATH,"//div[text()='Companies']")
act = ActionChains(driver)
act.move_to_element(comp_ele).perform()
time.sleep(5)
driver.find_element(By.XPATH,"//div[text()='IT companies']").click()
