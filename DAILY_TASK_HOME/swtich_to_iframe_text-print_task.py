from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
driver.maximize_window()
driver.find_elements(By.CLASS_NAME,"w3-btn w3-margin-bottom")
driver.switch_to.frame("iframeResult")
lin_text=driver.find_element(By.XPATH,"//h1[text()='The iframe element']").text
print(lin_text)

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[contains(@title,'W3Schools Free Online')]"))

text=driver.find_element(By.LINK_TEXT,"JavaScript Tutorial").text
print(text)