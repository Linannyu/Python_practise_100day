from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from information import *

options = Options()
options.add_argument(' --no-sandbox')
# 保持浏览器打开状态（默认是代码执行完毕自动关闭）
options.add_experimental_option("detach", True)

#创建并启动浏览器
driver = webdriver.Chrome(options=options)
driver.get('https://dmv.ny.gov/driver-license/prepare-for-and-take-your-permit-test')
driver.find_element(By.XPATH,"//span[normalize-space()='Get Pre-Screened']").click()
time.sleep(1)

# Prepare to Visit the DMV
driver.find_element(By.ID,"Dd-g_1").click()
driver.find_element(By.ID,"Dd-k_1").click()
## smbuit
driver.find_element(By.ID,"caption2_Dd-21").click()
time.sleep(1)

driver.find_element(By.ID,"caption2_Dc-m").click()
time.sleep(1)
driver.find_element(By.ID,"caption2_Dc-n1-1").click()
time.sleep(1)

# Document Guide
# 1
driver.find_element(By.ID,"ic_Dd-h1-1").click()
time.sleep(1)
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

# 2
driver.find_element(By.ID,"Dd-i2-1").click()
time.sleep(1)
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"Dd-33_1").click()
time.sleep(1)
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"caption2_Dd-14").click()
time.sleep(1)
driver.find_element(By.ID,"Dd-r3-16").click()
driver.find_element(By.ID,"Dd-r3-27").click()
driver.find_element(By.ID,"action_1").click()
time.sleep(1)


driver.find_element(By.ID,"Dd-c4_0").click()
driver.find_element(By.ID,"action_1").click()
time.sleep(1)
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

# apply for a learner permit
driver.find_element(By.ID,"caption2_Dc-n1-2").click()
time.sleep(1)
driver.find_element(By.ID,"Dd-m").send_keys(first_name)
driver.find_element(By.ID,"Dd-o").send_keys(last_name)
driver.find_element(By.ID,"Dd-q").send_keys(Dob)
sex = Select(driver.find_element(By.ID, "Dd-r"))
sex.select_by_visible_text("Female")
driver.find_element(By.CLASS_NAME,"IconCaptionText").click()
time.sleep(1)
driver.find_element(By.ID,"Dd-u").send_keys(high)
eye = Select(driver.find_element(By.ID, "Dd-y"))
eye.select_by_visible_text("Black")
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"Dd-a1_0").click()
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"Dd-g1").send_keys(email)
driver.find_element(By.ID,"Dd-h1").send_keys(email)
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"Dd-p1").send_keys(Street)
Type = Select(driver.find_element(By.ID, "Dd-q1"))
Type.select_by_visible_text("APARTMENT")

driver.find_element(By.ID,"Dd-r1").send_keys(Unit)
driver.find_element(By.ID,"Dd-s1").send_keys(City)
driver.find_element(By.ID,"Dd-u1").send_keys(Zip)
Conuty = Select(driver.find_element(By.ID, "Dd-v1"))
Conuty.select_by_visible_text("KINGS")
driver.find_element(By.ID,"Dd-y1_1").click()
input("请在浏览器中完成操作，完成后按 Enter 继续...")
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"Dd-62_1").click()
driver.find_element(By.ID,"bg_Dd-b2_1").click()
driver.find_element(By.ID,"bg_Dd-d2_1").click()
driver.find_element(By.ID,"Dd-e2_1").click()
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"Dd-s2_1").click()
driver.find_element(By.ID,"Dd-y2").click()
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"Dd-f3").click()
driver.find_element(By.ID,"action_1").click()
time.sleep(1)

driver.find_element(By.ID,"action_1").click()
time.sleep(1)

# Download the application form
driver.find_element(By.ID,"caption2_Dc-n1-3").click()
time.sleep(1)
driver.find_element(By.ID,"Dd-p_1").click()
driver.find_element(By.ID,"action_1").click()
time.sleep(1)