#xpath example,taking all values forday,month,year,navigation,locater,headless,handle,automatically clos,dropdowen handling,absolute xpath will pratish in rediff.com
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome()
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
driver.implicitly_wait(30)
h2_text=driver.find_element(By.XPATH,"//input[contaionstext(),'Full Name']").send_keys("murugan")


