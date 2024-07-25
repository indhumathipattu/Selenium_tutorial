#mouse events point means nama mose entha events ku mela vaikanumo antha events vakaika entha method
#athuku 1. url la veriyable store panaum then accthion chain ()kula driver koduanum athaium veriyable stroe panaum
#veriyable.koduthu move to element kotuthu thukula url veriyable kodukanum ethu ku neme tha mouseevent.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#mouse_double_click2 method
opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
#driver.get("https://www.naukri.com/")mouse event method
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(5)
#comp_ele = driver.find_element(By.XPATH,"//div[text()='Companies']") mouse event method
#act=ActionChains(driver)m.e
#act.move_to_element(comp_ele)m.e
#driver.find_element(By.XPATH,"//div[text()='Companies']").click()m.e
act1=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
chain=ActionChains(driver)
chain.double_click(act1).perform()
alter=driver.switch_to.alert


