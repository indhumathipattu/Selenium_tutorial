from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.rediff.com/")
driver.maximize_window()
win_text1 = driver.find_element(By.XPATH,"//a[@title='Lightning fast free email']").text
print(win_text1)
#driver.switch_to.frame("moneyiframe")  # id or name
#driver.switch_to.frame(0)   # index basis
ele = driver.find_element(By.XPATH,"//iframe[@title='Rediff Money Widget']")
driver  .switch_to.frame(ele)   # WebElement
frame_text = driver.find_element(By.XPATH,"//span[text()='BSE']").text
print(frame_text)
driver.switch_to.default_content()
win_text2 = driver.find_element(By.PARTIAL_LINK_TEXT,"Money").text
print(win_text2)


#https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe
#task for today i rame print
#jave scrit