from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from basics.Taking_Screenshot import opt

pt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
#driver.save_screenshot("C:\\Users\\mathi\\Desktop\\Screenshot\\screenshor3.png")
driver.refresh()
driver.forward()
atual_url=driver.current_url
print("atual_url")
actul_title=driver.title
print(actul_title)
driver.close()