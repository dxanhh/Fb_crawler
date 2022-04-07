# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:15:18 2021

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 08:33:00 2021

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:01:43 2021

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:19:21 2021

@author: Admin
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

list_tk_clone = ['0846078999','frost.wyrm318@gmail.com','0855112000',"hoangtrung20223108@gmail.com",'anhtuan3182022@gmail.com','anhtuan3192022@gmail.com']
list_mk_clone = ['37759386vy','12345678hihi','luongvuthien15102000',"Thang202111!","Thang202111!","Thang202111!"]

today = date.today()
d1 = today.strftime("%d/%m/%Y")

# Yesterday date
yesterday = today - timedelta(days = 1)
d2 = yesterday.strftime("%d/%m/%Y")

folder = r"C:/batfile/set up server/crawl facebook"


#danh sách link fb cá nhân
g = open('uid_tau_hoa_clean.txt', "r")
link1 = g.readlines()

#cache file
cachefile = folder+'/cache/cache.txt' 
h = open(cachefile, "r")
cache = h.readlines()
numb = cache[0]
stt = int(numb)
print(stt)
for loop in range(0,1000):
    try:
        #đăng nhập vào facebook
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        os.chdir(folder)
        print("dangnhap")
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        pref2 = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",pref2)
        driver.get('https://www.facebook.com/') 
        driver.maximize_window()
        sleep(0)
        table = driver.find_element_by_class_name('_9vtf')
        rows = table.find_elements_by_tag_name('div')
        account = randint(2, 4)
        # account = 2
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
            # action = 3
            #giả vờ lướt newfeed để facebook không chặn
            if action ==1:
                driver.get('https://m.facebook.com/') 
                print('luot newfeed')
                ##luot_new_feed
                scroll = randint(7, 10)
                while scroll < 5:
                    sleep(randint(1, 3))
                    scroll+=1
                    scroll1 = randint(300, 800)
                    driver.execute_script("window.scrollBy(0,{})".format(scroll1),"")
            if action ==2:
                #click_story
                driver.get('https://m.facebook.com/') 
                try:
                    sleep(5)
                    story = driver.find_element_by_xpath("//div[@class='_6m42 nineBySixteen']")
                    story.click()
                    sleep(randint(2, 3))
                    close = driver.find_element_by_xpath("//i[@data-sigil='m-stories-close-story-button']").click()
                except:
                    continue
            if action ==3:
                print('laythongtin')
                try:
                    driver.get(link1[stt])
                    sleep(randint(5, 7))
                    stt+=1
                    with open(cachefile, 'w',encoding="utf-8") as out:
                        out.write(str(stt))
                    #lấy thông tin cá nhân
                    name = driver.find_element_by_class_name('_6j_c').text
                    
                    info = driver.find_element_by_xpath("//div[@id='profile_intro_card']").click()
                    # info = driver.find_element_by_xpath("//div[contains(text(),'About info')]").click()
                    sleep(randint(3, 5))
                    
                    last_height = driver.execute_script("return document.body.scrollHeight")
                    l = 0 
                    while l < 5:
                        l+=1
                        # Scroll down to bottom
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        sleep(1)
                    driver.execute_script("window.scrollTo(0,0)","")
                    try:
                        edu = driver.find_element_by_xpath("//div[@id='education']").text
                        edu = (edu.replace("EDUCATION","")).replace("\n"," ")
                    except:
                        edu = "null"
                    try:
                        work = driver.find_element_by_xpath("//div[@id='work']").text
                        work = (work.replace("WORK","")).replace("\n"," ")
                    except:
                        work = "null"
                    try:
                        living = driver.find_element_by_xpath("//div[@id='living']").text
                        living = (living.replace("PLACES LIVED","")).replace("\n"," ")
                    except:
                        living = "null"
                    try:
                        contact_info = driver.find_element_by_xpath("//div[@id='contact-info']").text
                        contact_info = (contact_info.replace("CONTACT INFO","")).replace("\n"," ")
                    except:
                        contact_info = "null"
                    try:
                        basic_info = driver.find_element_by_xpath("//div[@id='basic-info']").text
                        basic_info = (basic_info.replace("BASIC INFO","")).replace("\n"," ")
                    except:
                        basic_info = "null"
                    try:
                        relationship = driver.find_element_by_xpath("//div[@id='relationship']").text
                        relationship = (relationship.replace("RELATIONSHIP","")).replace("\n"," ")   
                    except:
                        relationship = "null"
                        
                    try:
                        bio = driver.find_element_by_xpath("//div[@id='bio']").text
                        bio = (bio.replace("BIO","")).replace("\n"," ")   
                    except:
                        bio = "null"
                    tonghop = driver.find_elements_by_xpath("//div[@class='_55wo _2xfb _1kk1']")
                    
                    for i in tonghop:
                        if "CHECK-INS" in i.text:
                            checkin = i.text
                            checkin = (checkin.replace("CHECK-INS","")).replace("\n"," ")   
                            
                        if "SPORTS" in i.text:
                            sport = i.text
                            sport = (sport.replace("CHECK-INS","")).replace("\n"," ")   
                            
                        if "MUSIC" in i.text:
                            music = i.text
                            music = (music.replace("MUSIC","")).replace("\n"," ")   
                            
                        if "FILMS" in i.text:
                            films = i.text
                            films = (films.replace("FILMS","")).replace("\n"," ")   
                            
                        if "TV PROGRAMMES" in i.text:
                            tv = i.text
                            tv = (tv.replace("TV PROGRAMMES","")).replace("\n"," ")   
                            
                        if "BOOKS" in i.text:
                            books = i.text
                            books = (books.replace("BOOKS","")).replace("\n"," ")   
        
                        if "APPS AND GAMES" in i.text:
                            app = i.text
                            app = (app.replace("APPS AND GAMES","")).replace("\n"," ")
        
                        if "LIKES" in i.text:
                            likes = i.text
                            likes = (likes.replace("LIKES","")).replace("\n"," ")
        
                    backup_info = driver.find_element_by_id('viewport').text
                    backup_info = backup_info.replace("\n"," ") 
                    
                    infofile = name + ".json"
                    
                    # lấy link 10 post gần nhất    
                    back = driver.find_element_by_class_name('_6j_c').click()
                    sleep(randint(3, 5))
                    linkpost = name + ".txt"
                    os.chdir(folder+"/linkpost")
                    # Get scroll height
                    last_height = driver.execute_script("return document.body.scrollHeight")
                    l = 0 
                    while l < 10:
                        l+=1
                        # Scroll down to bottom
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        sleep(randint(2, 5))
                    driver.execute_script("window.scrollTo(0,0)","")
                    c = driver.find_elements_by_xpath('//div[@class="story_body_container"]/following-sibling::footer//a')
                    for d in c:
                        link2 = d.get_attribute('href')
                        if link2 is not None:
                            if "sharer" not in link2:
                                if 'focus' not in link2:
                                    with open(linkpost, 'a',encoding="utf-8") as out:
                                        out.write(link2 + '\n')
                    
                    #lấy content và comment các 10 post gần nhất
                    f = open(linkpost, "r")
                    link3 = f.readlines()
                    # content_data = {}
                    content_data = []
                    
                    if len(link3) < 10:
                        print('bo qua clone !')
                        os.remove(folder+"/info/"+infofile)
                        continue
                    else:
                        contentfile = name + ".json"
                        for e in range(0,10):
                            try:
                                comment_data = []
                                sleep(randint(5, 7))
                                driver.get(link3[e])
                                content = driver.find_element_by_class_name('story_body_container').text
                                # content1 = content.find_element_by_xpath("//div[@class='_5rgt _5nk5']")
                                time = driver.find_element_by_xpath("//div[@class='_52jc _5qc4 _78cz _24u0 _36xo']").text
                                content = content.replace(time,"")
                                content_text = ""
                                if "hrs" in time:
                                    time = d1
                                if "Yesterday" in time:
                                    time = time.replace("Yesterday",d2)
                                # try:
                                #     content11 = content1.find_element_by_xpath("//span[@class='_2z79']").text
                                #     # print(content11)
                                #     content_text += content11 + " "
                                # except NoSuchElementException:
                                #     content12 = content1.text
                                #     # print(content12)
                                #     content_text = content12 + " "
                                #     content_text += ((content_text.replace(name + '\n',' ')).replace('\n See translation','')).replace('\n',' ')     
                                # try:
                                #     content2 = content.find_element_by_xpath("//div[@class='_3q6s _78cw']").text
                                #     # print(content2)
                                #     content_text += content12 + " "
                                
                                # except NoSuchElementException:
                                #     pass
                                # try:
                                #     content3 = content1.find_element_by_xpath("//section[@class='_32l5 _2rec']").text
                                #     # print(content3)
                                #     content_text += content3 + " "
                                # except:
                                #     pass
                                content_text = ((content.replace(name,' ')).replace('See translation','')).replace('\n',' ')
                                table = driver.find_elements_by_class_name('_2a_m')
                                for b in table:
                                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    try:
                                        b.click()
                                        sleep(randint(2, 5))
                                    except ElementNotInteractableException:
                                        pass
                                #lay comment
                                comments = driver.find_elements_by_class_name('_2b06')
                                for a in comments: 
                                    try:
                                        ten = a.find_element_by_class_name('_2b05').text
                                        if name in ten:
                                            comment = a.text
                                            comment_data.append(comment.replace(name+"\n",""))
                                    except:
                                        pass
                                content_data.append({
                                        'time':time,
                                        'content' : content_text,
                                        'comment' : comment_data
                                        })
                                comment_data = []
                            except NoSuchElementException:
                                pass
                        data = {}
                        try:
                            data['name']  = name
                        except:
                            data['name']  = "null"
                        try:
                            data['education']  = edu
                        except:
                            data['education']  = 'null'
                        try:
                            data['work']  = work
                        except:
                            data['work']  = "null"
                        try:
                            data['placelive']  = living
                        except:
                            data['placelive']  = "null"
                        try:
                            data['contact_info']  = contact_info
                        except:
                            data['contact_info'] ="null"
                        try:
                            data['basic_info']  = basic_info
                        except:
                            data['basic_info']  = "null"
                        try:
                            data['relationship']  = relationship
                        except:
                             data['relationship']  = "null"
                        try:
                            data['bio']  = bio
                        except:
                            data['bio']  = "null"
                        try:
                            data['checkin']  = checkin
                        except:
                            data['checkin']  = "null"
                        try:
                            data['sport']  = sport
                        except:
                            data['sport']  = "null"
                        try:
                            data['music']  = music
                        except:
                            data['music'] = "null"
                        try:
                            data['films'] = films
                        except:
                            data['films'] = "null"
                        try:
                            data['television']  = tv
                        except:
                            data['television'] = "null"
                        try:
                            data['books']  = books
                        except:
                            data['books']  = "null"
                        try:
                            data['app']  = app
                        except:
                            data['app']  = "null"
                        try:
                            data['likes']  = likes
                        except:
                            data['likes'] = "null"
                        try:
                            data["backup_info"] = backup_info
                        except:
                            data["backup_info"] = "null"
                        try:
                            data['contents'] = content_data
                        except:
                            data['contents'] = "null"
                                                 
                        os.chdir(folder+"/info")
                        with codecs.open(infofile, 'w',encoding="utf-8") as out:
                            json.dump(data,out,indent=1,ensure_ascii=False)
                        os.chdir(folder)
                        sleep(randint(3, 5))
                    
                except:
                    sleep(randint(3, 5))
                    continue
        driver.quit()
        sleep(randint(90,120))
    except NoSuchElementException:
        driver.quit()
        sleep(randint(60,90))
        continue


   
