from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.amazon.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element()

