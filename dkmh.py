# -*- coding: utf-8 -*-

import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium .webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from select import select
import subprocess
import platform

from dotenv import load_dotenv
load_dotenv('.env')

def dkmh(print_log = True):
    #hide driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://mybk.hcmut.edu.vn/dkmh/home.action')
    #login
    username_text = driver.find_element_by_name('username')
    username_text.send_keys(os.environ.get('USRNAME'))
    password_text = driver.find_element_by_name('password')
    password_text.send_keys(os.environ.get('PASSWORD'))
    password_text.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"dangKyMonHocForm.action")]')))
    form_button = driver.find_element_by_xpath('//a[contains(@href,"dangKyMonHocForm.action")]')
    form_button.click()

    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'table-striped')))

    grade_table = driver.find_element_by_class_name('table-striped')
    tbody = grade_table.find_element_by_tag_name('tbody')
    rows = tbody.find_elements_by_tag_name('tr')

    new = []
    for row in rows[:-1]:
        content = row.find_elements_by_tag_name('td')
        if len(content) > 2: 
            if 'Đợt 4' in content[2].text: row.click()
    
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, ".//button[contains(@onclick, \"dangKyMonHocFormShow('div-DangKyMonHoc')\")]")))
    dk_button = driver.find_element_by_xpath(".//button[contains(@onclick, \"dangKyMonHocFormShow('div-DangKyMonHoc')\")]")
    dk_button.click()

    dotdk_button = driver.find_element_by_id('dotDKId445')
    dotdk_button.click()

    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'txtMSMHSearch')))
    msmh_input = driver.find_element_by_id('txtMSMHSearch')
    msmh_input.send_keys('CO3029')
    msmh_input.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'monHoc15561')))
    
    co3029_button = driver.find_element_by_id('monHoc15561')
    co3029_button.click()

    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, ".//button[contains(@onclick, \"dangKyNhomLopMonHoc(this, 740003, 15561)\")]")))
    
    dknhom_button = driver.find_element_by_xpath(".//button[contains(@onclick, \"dangKyNhomLopMonHoc(this, 740003, 15561)\")]")
    dknhom_button.click()

    wait = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "btnXacNhanKetQua")))
    
    xacnhan_button = driver.find_element_by_id('btnXacNhanKetQua')
    xacnhan_button.click()

    time.sleep(0.5)
    wait = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "btnXacNhanKetQua")))
    
    xacnhan_button1 = driver.find_element_by_id('btnXacNhanKetQua')
    xacnhan_button1.click()


    driver.save_screenshot('out.png')
    

if __name__ == '__main__':
    # dkmh()
    # time.sleep(300)
    while 1: 
        try:
            if len(sys.argv) > 1: dkmh(print_log=False)
            else: dkmh()
            print(f"Last modified: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        except Exception as e: 
            print(e)
        
        # time.sleep(300)


    
