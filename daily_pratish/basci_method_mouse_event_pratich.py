from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com/")
driver.maximize_window()
driver.implicitly_wait(30)
text1_place=driver.find_element(By.ID,"email").get_attribute("placeholder")
print(text1_place)
text2=driver.page_source
print(text2)
text3=driver.find_element(By.ID,"email").value_of_css_property("hight")
print(text3)
text4=driver.find_element(By.ID,"email").value_of_css_property("color")
print(text4)

text6=driver.find_element(By.ID,"email").value_of_css_property("fornt size")
print(text6)
driver.find_element(By.ID,"email").send_keys("indhumathi")
text7=driver.find_element(By.ID,"email").get_attribute("value")
print(text7)


# cookies not don