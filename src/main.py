from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

web_driver = webdriver.Edge(service=Service(r'G:\IDM Downloads\edgedriver_win64\msedgedriver.exe'))

print('selenium is running on ' + web_driver.name + ' with version :')

web_driver.get('https://www.bilibili.com/')

element = web_driver.find_element(By.CLASS_NAME, 'header-login-entry')
print('-----------' + element.id)
element.click()

time.sleep(2)

element = web_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/form/div[1]/input')
element.send_keys('the.lumw@gmail.com')

element = web_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/form/div[3]/input')
element.send_keys('DavidVilla?0622')


element = web_driver.find_element(By.CLASS_NAME, 'btn_primary')
element.click()

input()

pass