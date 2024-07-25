import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#opt=Options()
#opt.add_experimental_option("detach",True)
#driver = webdriver.Chrome(options=opt)
#driver.get("http://www.rediff.com")
#driver.maximize_window()
#time.sleep(5)
#print(driver.execute_script("document.element.scrollHeight"))
#time.sleep(5)
#driver.execute_script("window.scrollBy(0,2000)")
#time.sleep(5)
#driver.execute_script("window.scrollBy(0,-1000)")


# pratich test automation task pratich
opt = Options()
opt.add_experimental_option("detach", True)
#global driver
driver = webdriver.Chrome(options=opt)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("student")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
login = driver.find_element(By.XPATH,"//strong[contains(text(),'Congratulations student. You successfully logged in!')]").text

                                   # assert login == "Congratulations student. You successfully logged in!"