from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from password import *


options = Options()

# 使用 Selenium 专用的 Chrome 用户数据目录
options.add_argument(
    "--user-data-dir=/Users/lin./Documents/Python_practise_100day/5.School/SeleniumChromeProfile"
)

# Python 程序结束后保留 Chrome 窗口

options.add_experimental_option("detach", True)

print('1.Classroom\n2.College Board\n3.Overgrad')
user = input('请输入想要选择的网页编号：')

driver = webdriver.Chrome(options=options)


if user == '1':
    driver.get("https://classroom.google.com/")
elif user == '2':
    driver.get("https://prod.idp.collegeboard.org/oauth2/aus3koy55cz6p83gt5d7/v1/authorize?client_id=0oa3koxakyZGbffcq5d7&response_type=code&scope=openid%20email%20profile&redirect_uri=https://account.collegeboard.org/login/exchangeToken&state=cbAppDurl&nonce=-0-icO287JoECt-IHxTl0Q")
    time.sleep(1)
    driver.find_element(By.ID, "input28").send_keys(account + Keys.ENTER)
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
    driver.get("https://digital.fidelity.com/ftgw/digital/portfolio/balances")