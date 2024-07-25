import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#accept(), dismiss(), text

opt = Options()
opt.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opt)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME, "proceed").click()
time.sleep(5)
alt = driver.switch_to.alert
#alt.dismiss()  # cancel button

print(alt.text)

alt.accept()


#alat
#dismiss
#switch to alt(inspect pana mutiyatha ok button drive ku convert panurathuku
#text athula iruka tx print panurathuku