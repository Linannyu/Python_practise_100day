from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import time
from password import *


options = Options()

# 使用 Selenium 专用的 Chrome 用户数据目录
options.add_argument(
    "--user-data-dir=/Users/lin./Documents/Python_practise_100day/Py/5.Day_Tool/SeleniumChromeProfile"
)

# Python 程序结束后保留 Chrome 窗口

options.add_experimental_option("detach", True)

print('1.Classroom\n2.College Board\n3.Overgrad \n4.ConEdison \n5.nationalgrid \n6.DeltaMath')
user = input('请输入想要选择的网页编号：')

driver = webdriver.Chrome(options=options)


if user == '1':
    driver.get("https://classroom.google.com/")

elif user == '2':
    driver.get("https://prod.idp.collegeboard.org/oauth2/aus3koy55cz6p83gt5d7/v1/authorize?client_id=0oa3koxakyZGbffcq5d7&response_type=code&scope=openid%20email%20profile&redirect_uri=https://account.collegeboard.org/login/exchangeToken&state=cbAppDurl&nonce=-0-icO287JoECt-IHxTl0Q")
    time.sleep(1)
    driver.find_element(By.ID, "input28").send_keys(accounts + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, "input56").send_keys(collegeboard_Password + Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "a.cb-btn-primary").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue']").click()

elif user == '3':
    driver.get("https://app.overgrad.com/login")
    driver.find_element(By.CSS_SELECTOR, ".g-signin2").click()

elif user == '4':
    driver.get("https://webpayments.billmatrix.com/ConEdResidential")
    # 输入Con的Account Number
    driver.find_element(By.ID, "BillAccountNumber").send_keys(con_account)
    # 输入Email
    driver.find_element(By.ID, "EmailAddress").send_keys(accounts)
    # 点击Continue
    driver.find_element(By.ID, "btnContinue").click()
    time.sleep(3)
    bank_CVV = input('Plese enter your bank Security Code: ')
    driver.find_element(By.ID, "PaymentInfoList_0__CardWallet_SecurityCode").send_keys(bank_CVV)
    time.sleep(1)
    driver.find_element(By.ID, "btnContinue").click()
    time.sleep(3)

elif user == '5':
    driver.get("https://internet.speedpay.com/nationalgrid/#/login/guest")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button.dropdown-toggle.btn.btn-outline-primary").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "dropdown-item").click()
    driver.find_element(By.ID, "sp_account_number").send_keys(nation_account)
    driver.find_element(By.ID, "ui_field_grid").send_keys('Lin')
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary.login-btn.btn.btn-blue.primary-background-color.primary-border-color").click()
    time.sleep(2)
    driver.find_element(By.ID, "sp_cust_first_name").send_keys(fafi_name)
    driver.find_element(By.ID, "sp_cust_last_name").send_keys(fala_name)
    driver.find_element(By.ID, "sp_cust_email1").send_keys(accounts)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.primary-background-color.primary-border-color").click()
    time.sleep(2)

    bank_number = input('Plese enter your bank number: ')
    bank_CVV = input('Plese enter your bank Security Code: ')
    bank_Good_Thru_Date = input('Plese enter your bank Good Thru Date: ')
    zip_code = input('Plese enter your zip code: ')
    
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "sp_card_card_number").send_keys(bank_number)
    exp_date = driver.find_element(By.ID, "sp_card_exp_date")
    exp_date.click()
    time.sleep(1)
    exp_date.send_keys(bank_Good_Thru_Date)
    driver.find_element(By.ID, "sp_card_debit_zip").send_keys(zip_code)
    driver.find_element(By.ID, "sp_card_debit_cvv").send_keys(bank_CVV)
    time.sleep(2)
    next = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.primary-background-color.primary-border-color")
    driver.execute_script("arguments[0].click();", next)
    time.sleep(2)
    review = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.primary-background-color.primary-border-color").click()
    driver.execute_script("arguments[0].click();", review)

elif user == '6':
    driver.get("https://www.deltamath.com/sign-in?redirectUrl=student/5403260/33307131/d45e43e9f5e41d7aa66c041fb8d958be")
    driver.find_element(By.CLASS_NAME, "nsm7Bb-HzV7m-LgbsSe-BPrWId").click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1]) # 切换到新窗口
    driver.find_element(By.CLASS_NAME, "LbOduc").click()
    time.sleep(3)
    driver.find_element(By.ID, "username").send_keys(School_Email + Keys.ENTER)
    driver.find_element(By.ID, "password-input").send_keys(School_Password + Keys.ENTER)
