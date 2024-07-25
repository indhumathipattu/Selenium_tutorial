from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com/")
driver.maximize_window()
attr_text = driver.find_element(By.ID,"email").get_attribute("aria-label")
print(attr_text)

text2 = driver.page_source
print(text2)

text3 = driver.find_element(By.ID,"email").value_of_css_property("color")
print(text3)
text4 = driver.find_element(By.ID,"email").value_of_css_property("font-size")
print(text4)

text5 = driver.find_element(By.ID,"email").value_of_css_property("height")
print(text5)

driver.find_element(By.ID,"email").send_keys("indumathi")

text6 = driver.find_element(By.ID,"email").get_attribute("value")
print(text6)

print(driver.get_cookie('sb'))

list_cookie = driver.get_cookies()
print(len(list_cookie))

for i in list_cookie:
    print(i.get('name'))
