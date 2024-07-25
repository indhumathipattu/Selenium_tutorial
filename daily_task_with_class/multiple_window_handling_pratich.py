import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#from basics.Multiple_window_handling import child

opt =Options()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
print("parent_window_tittle=",driver.tittle)
driver.find_element(By.ID,"terms-link").click()
parent_window=driver.current_window_handle
child1_window=driver.window_handles
for child in child1_window:
    if  parent_window != child:
        driver.switch_to.window(child)
        time.sleep(5)
        print("Child window title = ", driver.title)
        child_win_text = driver.find_element(By.XPATH,"//h2[text()='Terms of Service']").text
        print(child_win_text)

driver.switch_to.window(parent_window)
driver.find_element(By.NAME,"firstname").send_keys("indumathi")
time.sleep(5)
driver.quit()
