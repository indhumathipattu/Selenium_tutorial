import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Datadriven import excel_reader


driver =webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
excel_path ="C:\\Users\\mathi\\Desktop\\Book1.xlsx"
rows =excel_reader.getRowCount(excel_path,"Sheet1")
for i in range(2,rows+1):
    un=excel_reader.readData(excel_path,"Sheet1",r,1)
    ps =excel_reader.readData(excel_path,"Sheet11",r,2)
    time.sleep(5)
    driver.find_element(By.NAME,"username").send_keys(un)
    time.sleep(3)
    driver.find_element(By.NAME,"password").send_keys(ps)
    time.sleep(30)
    driver.find_element(By.XPATH,"//button[normalize-space(text()='login'])").click()
    time.sleep(30)
    actual_title=driver.title
    if actual_title == "OrangeHRM":
        excel_reader.writeData(excel_path,"Sheet1",r,3,"pass")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT,"Logout").click()
        time.sleep(3)
    else:
        excel_reader.writeData(excel_path, "Sheet1", r, 3, "fail")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(3)

