import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium .webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from select import select
import subprocess
import platform

from dotenv import load_dotenv
load_dotenv('.env')

#hide driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get('http://mybk.hcmut.edu.vn/stinfo/')

#login
username_text = driver.find_element_by_name('username')
username_text.send_keys(os.environ.get('USRNAME'))
password_text = driver.find_element_by_name('password')
password_text.send_keys(os.environ.get('PASSWORD'))
password_text.send_keys(Keys.RETURN)

#get grade table
grade_button = driver.find_element_by_partial_link_text("Bảng điểm")
grade_button.click()
wait = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'content-tab-table')))

grade_table = driver.find_element_by_class_name('content-tab-table')
tbody = grade_table.find_element_by_tag_name('tbody')
rows = tbody.find_elements_by_tag_name('tr')

new = []
for row in rows[:-1]:
    content = row.find_elements_by_tag_name('td')
    if len(content) > 1:
        new += [content[1].text + '\t' + content[-1].text + '\n']

#compare with old table
f = open('out.txt')
old = f.readlines()

isUpdate = False
for o, n in zip(old, new):
    if o != n: 
        if not isUpdate: 
            print(f"Press any key to exit...")
            
        print(n[:-1]) #ignore endline
        subprocess.Popen(['notify-send',n[:-1]])

        if not isUpdate:
            if platform.system() == 'Linux':
                while 1:
                    os.system('play -nq -t alsa synth 1 sine 440') #Beep
                    rlist, _, _ = select([sys.stdin], [], [], 1)
                    if rlist: break                
            elif platform.system() == 'Windows':
                #TODO: Beep for Windows
                pass
        
        isUpdate = True
f.close()

#write new grade table
f = open('out.txt','w')
f.writelines(new)
f.close()


    
