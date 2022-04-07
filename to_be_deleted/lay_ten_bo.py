
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

list_tk_clone = ['frost.wyrm318@gmail.com','0855112000',"hoangtrung20223108@gmail.com",'anhtuan3182022@gmail.com','anhtuan3192022@gmail.com']
list_mk_clone = ['12345678hihi','luongvuthien15102000',"Thang202111!","Thang202111!","Thang202111!"]


folder = r"C:\batfile\set up server\crawl facebook"


#danh sách link fb cá nhân
g = open('uid2.txt', "r")
link1 = g.readlines()

#cache file
cachefile = folder+'\cache\cache.txt' 
h = open(cachefile, "r")
cache = h.readlines()
numb = cache[0]
stt = int(numb)
print(stt)

for loop in range(0,10000):
    try:
        #đăng nhập vào facebook
        os.chdir(folder)
        print("dangnhap")
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.facebook.com/') 
        driver.maximize_window()
        sleep(0)
        table = driver.find_element_by_class_name('_9vtf')
        rows = table.find_elements_by_tag_name('div')
        account = randint(1,4)

        for a in rows:
            tendangnhap = a.find_element_by_id('email')
            tendangnhap.send_keys(list_tk_clone[account])
            sleep(randint(1, 3))
            matkhau = a.find_element_by_id('pass')
            matkhau.send_keys(list_mk_clone[account]) 
            sleep(randint(1, 3))
            break
        dangnhap = table.find_element_by_class_name('_6ltg').click()
        sleep(randint(3, 5))
               
        for actions in range(0,20):
        # actions = 0
        # while actions < 20:
        #     actions +=1
            print('vong lap thu: '+ str(actions))
            action = randint(1, 3)
            # action = 2
            #giả vờ lướt newfeed để facebook không chặn
            if action ==1:
                driver.get('https://m.facebook.com/') 
                print('luot newfeed')
                ##luot_new_feed
                scroll = randint(1, 10)
                while scroll < 10:
                    sleep(randint(2, 5))
                    scroll+=1
                    scroll1 = randint(300, 800)
                    driver.execute_script("window.scrollBy(0,{})".format(scroll1),"")
            # if action ==3:
            #     #click_story
            #     driver.get('https://m.facebook.com/') 
            #     try:
            #         sleep(5)
            #         story = driver.find_element_by_xpath("//div[@class='_6m42 nineBySixteen']")
            #         story.click()
            #         sleep(randint(2, 3))
            #         close = driver.find_element_by_xpath("//i[@data-sigil='m-stories-close-story-button']").click()
            #     except:
            #         continue
            if action ==2 or action ==3:
                print('laythongtin')
                try:
                    linkfull = "https://m.facebook.com/"+link1[stt]
                    driver.get(linkfull)
                    scroll1 = 200
                    driver.execute_script("window.scrollBy(0,{})".format(scroll1),"")
                    sleep(randint(5, 7))
         
                    #lấy thông tin cá nhân
                    name = driver.find_element_by_class_name('_6j_c').text
                    if name == "You can't use this feature at the moment":
                    	driver.quit()
                    	break	
                    if name == "You’re Temporarily Blocked":
                    	driver.quit()
                    	break
                    with open("uid_and_name3.txt",'a',encoding = "utf-8") as out:
                        out.write(name+"##"+link1[stt])
                    stt+=1
                    # print(str(stt))
                    with open(cachefile, 'w',encoding="utf-8") as out:
                        out.write(str(stt))
                    
                except:
                    sleep(randint(60, 90))
                    continue
        driver.quit()
        # sleep(randint(60,90))
        sleep(randint(3, 5))
    except NoSuchElementException:
        driver.quit()
        sleep(randint(60,90))
        continue


   
