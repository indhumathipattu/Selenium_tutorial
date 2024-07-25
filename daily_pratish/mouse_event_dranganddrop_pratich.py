from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from basics.Mouse_Events_DrangandDrop import f1

opt=Options()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
fe1 = driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(fe1)
ele1 = driver.find_element(By.ID,"draggable")
ele2 = driver.find_element(By.ID,"droppable")
act = ActionChains(driver)
act.drag_and_drop(ele1,ele2).perform()
