# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 12:36:45 2021

@author: Admin
"""

from time import sleep
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
import os.path
from random import randint

# folder = r"C:\Users\pc-admin\Desktop\VY-fbcrawling"
# #thêm link profile
# profile = "https://m.facebook.com/profile.php?id=100010037523944"
#driver = webdriver.Chrome()
link = []

list_tk_clone = ['0846078999','frost.wyrm318@gmail.com','0855112000']
list_mk_clone = ['37759386vy','12345678hihi','luongvuthien15102000']

#đăng nhập vào facebook
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
pref2 = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",pref2)
driver.get('https://www.facebook.com/') 
driver.maximize_window()
sleep(0)
table = driver.find_element_by_class_name('_9vtf')
rows = table.find_elements_by_tag_name('div')
account = randint(0, 2)
for a in rows:
    tendangnhap = a.find_element_by_id('email')
    tendangnhap.send_keys("0846078999")
    sleep(randint(1, 3))
    matkhau = a.find_element_by_id('pass')
    matkhau.send_keys('37759386vy') 
    sleep(randint(1, 3))
    break
dangnhap = table.find_element_by_class_name('_6ltg').click()
sleep(randint(3, 5))
driver.get('https://www.facebook.com/groups/hoivetau/members')
for a in range(0,10000):
    print(a)
    # action = randint(1, 2)
    # if action ==1:
    members = driver.find_elements_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p']")
    for a in members:
        uid = a.get_attribute("href")
        print(uid)
        with open("uid_tau_hoa.txt","a",encoding = "utf=8") as out:
            out.write(uid+"\n")
    # if action ==2:
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    l = 0 
    while l < 10:
        l+=1
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(randint(3, 5))
        # driver.execute_script("window.scrollTo(0,0)","")