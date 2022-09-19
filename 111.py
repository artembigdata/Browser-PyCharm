import selenium
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/artemislamowicloud.com/Documents/Jupiter_Notebook/управление браузером/chromedriver')
#driver = webdriver.Firefox(executable_path='/Users/artemislamowicloud.com/Documents/Jupiter_Notebook/управление браузером/geckodriver')

driver.get('https://lk.finam.ru/')
driver.maximize_window()
user_name = driver.find_element(By.ID, 'txauth-widget-login')

#user_name = driver.find_elements_by_class('txauth-widget-login')
#user_name.send_keys("artemislamov")

user_name.send_keys("555")








