from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.find_element(By.ID,"email").send_keys("indumathi")
driver.find_element(By.ID,"pass").send_keys("indhu@123")
driver.find_element(By.LINK_TEXT,"Create new account").click()
wait=WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.NAME,"firstname"))).send_keys("indhumathi")
driver.find_element(By.NAME,"lastname").send_keys('M')
driver.close()
