# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:05:53 2022

@author: Administrator
"""

from time import sleep
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
import os.path
from random import randint
import os
import codecs
import json

from datetime import date
from datetime import timedelta

    
folder = r"C:\batfile\set up server\crawl facebook"


#danh sách link fb cá nhân
g = open('list_UID_TNH_19_1.txt', "r")
link1 = g.readlines()

#cache file
cachefile = folder+'\cache\cache_25_1.txt' 
h = open(cachefile, "r")
cache = h.readlines()
numb = cache[0]
stt = int(numb)
print(stt)   
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
for i in range(0,10000):
    try:
        linkfull = "https://m.facebook.com/"+link1[stt]
        driver.get(linkfull) 
        scroll1 = 100
        driver.execute_script("window.scrollBy(0,{})".format(scroll1),"")
        name = driver.find_element_by_xpath("//h3[@class='_391s']").text
        print(name)
        stt+=1
        sleep(randint(5, 7))
        with open(cachefile, 'w',encoding="utf-8") as out:
            out.write(str(stt))
        with open("uid_and_name.txt",'a',encoding = "utf-8") as out:
            out.write(name+"##"+link1[stt])
    except:
        stt+=1
        with open(cachefile, 'w',encoding="utf-8") as out:
            out.write(str(stt))
        




   
