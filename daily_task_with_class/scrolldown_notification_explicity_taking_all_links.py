import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opt=Options()
opt.add_argument("__disable_notification")
driver = webdriver.Chrome(options=opt)
driver.get("https://www.facebook.com")
driver.maximize_window()
actul_url=driver.current_url
print(actul_url)
actul_tittle=driver.title
print(actul_tittle)
time.sleep(5)
driver.find_element(By.ID,"email").send_keys("indumathi")
driver.find_element(By.ID,"pass").send_keys("indhu@123")
driver.find_element(By.LINK_TEXT,"Create new account").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.NAME,"firstname"))).send_keys("Indhumathi")
time.sleep(5)
driver.execute_script("window.scrollBy(0,2000)")
driver.execute_script("window.scrollBy(0,-1000)")
time.sleep(3)
len_li=driver.find_elements(By.TAG_NAME,"a")
print(len_li)
for i in len_li:
    print(i.text,"--->",i.get_attribute("herf"))
