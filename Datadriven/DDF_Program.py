import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Datadriven import excel_reader

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
excel_Path = "C:\\Users\\pc\\Desktop\\DDF1.xlsx"
rows = excel_reader.getRowCount(excel_Path,"Sheet9")

for r in range(2,rows+1):
    un = excel_reader.readData(excel_Path,"Sheet9",r,1)
    pwd = excel_reader.readData(excel_Path,"Sheet9",r,2)

    time.sleep(3)
    driver.find_element(By.NAME,"username").send_keys(un)
    time.sleep(3)
    driver.find_element(By.NAME,"password").send_keys(pwd)
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
    actual_title = driver.title
    if actual_title == "OrangeHRM":
        excel_reader.writeData(excel_Path,"Sheet9",r,3,"Pass")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,"Logout").click()
    else:
        excel_reader.writeData(excel_Path,"Sheet9",r,3,"Fail")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Logout").click()