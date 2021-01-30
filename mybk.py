import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
load_dotenv('.env')

driver = webdriver.Chrome()
driver.get('http://mybk.hcmut.edu.vn/stinfo/')

username_text = driver.find_element_by_name('username')
username_text.send_keys(os.environ.get('USRNAME'))
password_text = driver.find_element_by_name('password')
password_text.send_keys(os.environ.get('PASSWORD'))
password_text.send_keys(Keys.RETURN)


