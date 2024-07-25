import time

import radio
from _testmultiphase import Example
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,"radioButton").click()
exam_rat=driver.find_element(By.XPATH,"//input[@class='radioButton'][@value='radio1']")
time.sleep(5)
#radio2
driver.find_element(By.NAME,"radioButton").click()
example_rat2=driver.find_element(By.XPATH,"//input[@class='radioButton'][@value='radio2']")
time.sleep(5)
#radiio3
driver.find_element(By.NAME,"radioButton").click()
example_3=driver.find_element(By.XPATH,"//input[@class='radioButton'][@value='radio3']")
time.sleep(5)
#check box,option1
driver.find_element(By.NAME,"checkBoxOption1").click()
che_box=driver.find_element(By.XPATH,"//input[@name='checkBoxOption1'][@value='option1']")
time.sleep(5)
#option2
driver.find_element(By.NAME,"checkBoxOption3").click()
che1_box=driver.find_element(By.XPATH,"//input[@id='checkBoxOption2'][@value='option2']")
#option3
driver.find_element(By.ID,"checkBoxOption3").click()
che2_box=driver.find_element(By.XPATH,"//input[@id='checkBoxOption3'][@value='option3']")
time.sleep(5)
#dispalay
ra1_exam1=exam_rat.is_displayed()
print("Radio Button Example displayed=",ra1_exam1)
#enable
ra2_exam2=exam_rat.is_enabled()
print("Radio Button Example=",ra2_exam2)
#selected
ra3_exam3=exam_rat.is_selected()
print("Radio Button Example=",ra3_exam3)
exam_rat.click()
ra3_exam3=exam_rat.is_selected()
print(" After clicking Radio Button Example selected =",ra3_exam3)
#display2
ra4_exam4=example_rat2.is_displayed()
print("Radio Button Example=",ra4_exam4)
#enable2
ra5_exam5=example_rat2.is_enabled()
print("Radio Button Example=",ra5_exam5)
#selected2
ra6_exam6=example_rat2.is_selected()
print("Radio Button Example=",ra6_exam6)
example_rat2.click()
ra6_exam6=example_rat2.is_selected()
print("After clicking Radio Button Example selected =",ra6_exam6)
time.sleep(5)
#display3
ra7_exam7=example_3.is_displayed()
print("Radio Button Example=",ra7_exam7)
#enable3
ra8_exam8=example_3.is_selected()
print("Radio Button Example=",ra8_exam8)
#selected3
ra9_exam9=example_3.is_selected()
print("Radio Button Example=",ra9_exam9)
example_3.click()
ra9_exam9=example_3.is_selected()
print("After clicking Radio Button Example selected =",ra9_exam9)
#auto_suggestion
driver.find_element(By.ID,"autocomplete").send_keys("Ind")
auto1_li=driver.find_elements(By.XPATH,"//div[@class='cen-left-align']//fieldset/input")
time.sleep(5)
for i in auto1_li:
    print(i.text)
    if i.text == "India":

        i.click()
#dropdown method
driver.find_element(By.ID,"dropdown-class-example").click()
driver.implicitly_wait(30)
select_select1=driver.find_element(By.XPATH,"//option[text()='Option1']")
mon_dd =driver.find_element(By.ID,"dropdown-class-example")
sel= Select(mon_dd)
sel.select_by_value("option1")
time.sleep(5)
sel.select_by_value("option2")
time.sleep(5)
sel.select_by_value('option3')
#chekbox example

#option1 is selected
cbox1=che_box.is_selected()
print("Checkbox Example=",cbox1)
#option1 is enabled
cbox2=che_box.is_enabled()
print("Checkbox Example=",cbox2)
#option1 is displayed
cbox3=che_box.is_displayed()
print("Checkbox Example=",cbox3)
cbox3=che_box.click()
print("After clicking checkbox Example selected =",cbox3)
time.sleep(5)

#option2 is selected
cbox4=che1_box.is_selected()
print("checkbox Example=",cbox4)
#option2 is enabled
cbox5=che1_box.is_enabled()
print("checkbox Example=",cbox5)
#option2 is enabled
cbox6=che1_box.is_enabled()
print("checkbox Example=",cbox6)
#option2 is displayed
cbox7=che1_box.is_displayed()
print("checkbox Example=",cbox7)
cbox7=che_box.click()
print("After clicking checkbox Example selected =",cbox7)
driver.find_element(By.NAME,"checkBoxOption3").click()
time.sleep(5)

#option3 is selected
cbox8=che2_box.is_selected()
print("checkbox Example=",cbox8)
#option9 is enabled
cbox9=che2_box.is_enabled()
print("checkbox Example=",cbox9)
#option 10
cbox10=che2_box.is_displayed()
print("checkbox Example=",cbox10)
cbox10=che_box.click()
print("After clicking checkbox Example selected =",cbox10)
#Mouse Hover Example
mous1=driver.find_element(By.ID,"mousehover")
act2=ActionChains(driver)
act2.move_to_element(mous1).perform()
time.sleep(5)
#Web Table Example
wind1=driver.find_element(By.XPATH,"//td[text()='Master Selenium Automation in simple Python Language']").text
print(wind1)
#Switch To Alert Example
driver.find_element(By.ID,"confirmbtn").click()
time.sleep(5)
alt = driver.switch_to.alert
alt.accept()
time.sleep(5)
driver.find_element(By.ID,"confirmbtn").click()
alt=driver.switch_to.alert
alt.dismiss()
time.sleep(5)
#Switch Window Example
driver.find_element(By.ID,"openwindow").click()
driver.switch_to.default_content()
#Switch Tab Example
driver.find_element(By.ID,"opentab").click()
driver.switch_to.default_content()
#Element Displayed Example
driver.find_element(By.ID,"hide-textbox").click()
time.sleep(5)
#alrt1=driver.switch_to.alert

#driver.find_element(By.CLASS_NAME,"btn-style class2").click()

#switch to i frame
#win_text=driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']")
#driver.switch_to.frame(win_text)
#fra1_text=driver.find_element(By.LINK_TEXT,"All Access plan").text
#print(fra1_text)

