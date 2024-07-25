import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.PARTIAL_LINK_TEXT,"ate new").click()
driver.find_element(By.NAME,"firstname").send_keys("indumathi")
time.sleep(5)
act = ActionChains(driver)

act.send_keys(Keys.TAB).send_keys("M").send_keys(Keys.TAB).send_keys("indumathi@gmail.com").send_keys(Keys.TAB).send_keys("indumathi@gamil.com").send_keys(Keys.TAB).send_keys("indumathi@123").perform()


#https://www.flipkart.com/account/login?ret=/  TASK FOR flipcard.COM