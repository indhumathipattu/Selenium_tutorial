from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

#s = Service(executable_path='F:\\drives\\chromedriver-win64\\chromedriver.exe')
#driver = webdriver.Chrome(service=s)

opt = Options()
opt.add_experimental_option("detach",True)
driver =webdriver.Chrome(options=opt)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH("/html/body/div/div/div[1]/div[1]/di   v[2]/div[2]/form/div/div/input")).send_keys("redmi note 13 pro")
driver.find_element(By.XPATH, "html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div[1]/button").click()

original_window = driver.current_window_handle
all_windows = driver.window_handles

for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)


        try:

            pass
        except StaleElementReferenceException as e:
            print(e.msg)
            driver.close()


driver.switch_to.window(original_window)

#html/body/div/div/div[3]/div/div[2]/div/form/div[1]/div[2]/button