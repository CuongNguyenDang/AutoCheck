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

def crawl_score_ppl(print_log = True):
    #hide driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fe-learning.hcmut.edu.vn%2Flogin%2Findex.php%3FauthCAS%3DCAS')

    #login
    username_text = driver.find_element_by_name('username')
    username_text.send_keys(os.environ.get('USRNAME'))
    password_text = driver.find_element_by_name('password')
    password_text.send_keys(os.environ.get('PASSWORD'))
    password_text.send_keys(Keys.RETURN)

    driver.get('http://e-learning.hcmut.edu.vn/user/index.php?contextid=1103699&id=69025&perpage=5000')

    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Clear filters']")))
    time.sleep(1)
    
    driver.find_element_by_xpath("//button[text()='Clear filters']").click()
    driver.find_element_by_xpath("//button[text()='Apply filters']").click()
    time.sleep(3)
    tbody = driver.find_element_by_tag_name('tbody')
    a = tbody.find_elements_by_class_name('d-inline-block')
    urls = [x.get_attribute('href') for x in a]
    print('TOTAL: ',len(urls))

    f = open('out.csv','w')
    f.write('"Name","Score",\n')
    for url in urls:
        driver.get(url)

        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Điểm")))
        score_url = driver.find_element_by_partial_link_text('Điểm')
        score_url.click()

        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "page-header-headings")))
        name = driver.find_element_by_class_name('page-header-headings').text

        tr = driver.find_elements_by_tag_name('tr')[-2]
        score = tr.find_elements_by_tag_name('td')[1].text.replace(',','.')

        f.write('"{0}","{1}",\n'.format(name,score))
        print(name,'\t',score)

    f.close()
    

if __name__ == '__main__':
    crawl_score_ppl()

    
