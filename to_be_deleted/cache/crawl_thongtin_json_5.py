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


# from webdriver_manager.chrome import ChromeDriverManager


from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
import os.path
from random import randint
import os
import codecs
import json
from datetime import date
from datetime import timedelta
list_tk_clone = ['frost.wyrm318@gmail.com', '0855112000',
                 "hoangtrung20223108@gmail.com", 'anhtuan3182022@gmail.com', 'anhtuan3192022@gmail.com']
list_mk_clone = ['12345678hihi', 'luongvuthien15102000',
                 "Thang202111!", "Thang202111!", "Thang202111!"]

today = date.today()
d1 = today.strftime("%d/%m/%Y")

# Yesterday date
yesterday = today - timedelta(days=1)
d2 = yesterday.strftime("%d/%m/%Y")

folder = r"C:/batfile/set up server/crawl facebook"


# danh sách link fb cá nhân
g = open('BO_UID.txt', "r")
link1 = g.readlines()

# cache file
cachefile = folder+'/cache/cache_5_4.txt'
h = open(cachefile, "r")
cache = h.readlines()
numb = cache[0]
stt = int(numb)
print(stt)
for loop in range(0, 1000):
    try:
        # đăng nhập vào facebook
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # os.chdir(folder)
        print("dangnhap")
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        pref2 = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", pref2)
        driver.get('https://www.facebook.com/')
        driver.maximize_window()
        sleep(0)
        table = driver.find_element_by_class_name('_9vtf')
        rows = table.find_elements_by_tag_name('div')

        account = randint(0, len(list_tk_clone)-1)
        account = 3

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

        for actions in range(0, 20):
            print('vong lap thu: ' + str(actions))
            # action = randint(1, 3)
            action = 3
            # giả vờ lướt newfeed để facebook không chặn
            if action == 1:
                driver.get('https://m.facebook.com/')
                print('luot newfeed')
                # luot_new_feed
                scroll = randint(0, 5)
                for i in range(scroll, 10):
                    sleep(randint(1, 5))
                    scroll += 1
                    scroll1 = randint(100, 800)
                    driver.execute_script(
                        "window.scrollBy(0,{})".format(scroll1), "")
            if action == 2:
                sleep(randint(7, 10))
                print("sleeping")
                # #click_story
                # driver.get('https://m.facebook.com/')
                # try:
                #     sleep(5)
                #     story = driver.find_element_by_xpath("//div[@class='_6m42 nineBySixteen']")
                #     story.click()
                #     sleep(randint(2, 3))
                #     close = driver.find_element_by_xpath("//i[@data-sigil='m-stories-close-story-button']").click()
                # except:
                #     continue
            if action == 3:
                print('laythongtin')

                data = {}

                try:
                    driver.get('https://m.facebook.com/'+str(link1[stt]))

                    data["UID"] = str(link1[stt].replace("\n", ""))

                    sleep(randint(3, 5))
                    # lấy thông tin cá nhân

                    info = driver.find_element_by_xpath("//div[@id='profile_intro_card']").click()
                    sleep(randint(3, 5))

                    name = driver.find_element_by_class_name('_6j_c').text

                    print(name)

                    data['name'] = name

                    if "blocked" in name:
                        break
                        list_tk_clone.pop(account)
                        list_mk_clone.pop(account)
                        driver.quit()

                    if "moment" in name:
                        break
                        list_tk_clone.pop(account)
                        list_mk_clone.pop(account)
                        driver.quit()

                    scroll = randint(0, 5)

                    for i in range(scroll, 10):
                        sleep(randint(1, 3))
                        scroll1 = randint(300, 800)
                        driver.execute_script(
                            "window.scrollBy(0,{})".format(scroll1), "")

                    driver.execute_script("window.scrollTo(0,0)", "")

                    try:
                        edu = driver.find_element_by_xpath(
                            "//div[@id='education']").text
                        edu = (edu.replace("EDUCATION", "")).replace("\n", " ")
                        data['education'] = edu
                    except:
                        data['education'] = 'null'

                    try:
                        work = driver.find_element_by_xpath(
                            "//div[@id='work']").text
                        work = (work.replace("WORK", "")).replace("\n", " ")
                        data['work'] = work
                    except:
                        data['work'] = "null"

                    try:
                        living = driver.find_element_by_xpath(
                            "//div[@id='living']").text
                        living = (living.replace("PLACES LIVED", "")
                                  ).replace("\n", " ")
                        data['placelive'] = living
                    except:
                        data['placelive'] = "null"

                    try:
                        contact_info = driver.find_element_by_xpath(
                            "//div[@id='contact-info']").text
                        contact_info = (contact_info.replace(
                            "CONTACT INFO", "")).replace("\n", " ")
                        data['contact_info'] = contact_info
                    except:
                        data['contact_info'] = "null"

                    try:
                        basic_info = driver.find_element_by_xpath(
                            "//div[@id='basic-info']").text
                        basic_info = (basic_info.replace(
                            "BASIC INFO", "")).replace("\n", " ")
                        data['basic_info'] = basic_info
                    except:
                        data['basic_info'] = "null"

                    try:
                        relationship = driver.find_element_by_xpath(
                            "//div[@id='relationship']").text
                        relationship = (relationship.replace(
                            "RELATIONSHIP", "")).replace("\n", " ")
                        data['relationship'] = relationship
                    except:
                        data['relationship'] = "null"

                    try:
                        bio = driver.find_element_by_xpath(
                            "//div[@id='bio']").text
                        bio = (bio.replace("BIO", "")).replace("\n", " ")
                        data['bio'] = bio
                    except:
                        data['bio'] = "null"

                    tonghop = driver.find_elements_by_xpath(
                        "//div[@class='_55wo _2xfb _1kk1']")

                    for i in tonghop:
                        if "CHECK-INS" in i.text:
                            checkin = i.text
                            checkin = (checkin.replace(
                                "CHECK-INS", "")).replace("\n", " ")
                            data['checkin'] = checkin
                        else:
                            data['checkin'] = "null"

                        if "SPORTS" in i.text:
                            sport = i.text
                            sport = (sport.replace("CHECK-INS", "")
                                     ).replace("\n", " ")
                            data['sport'] = sport
                        else:
                            data['sport'] = "null"

                        if "MUSIC" in i.text:
                            music = i.text
                            music = (music.replace("MUSIC", "")
                                     ).replace("\n", " ")
                            data['music'] = music
                        else:
                            data['music'] = "null"

                        if "FILMS" in i.text:
                            films = i.text
                            films = (films.replace("FILMS", "")
                                     ).replace("\n", " ")
                            data['films'] = films
                        else:
                            data['films'] = "null"

                        if "TV PROGRAMMES" in i.text:
                            tv = i.text
                            tv = (tv.replace("TV PROGRAMMES", "")
                                  ).replace("\n", " ")
                            data['television'] = tv
                        else:
                            data['television'] = "null"

                        if "BOOKS" in i.text:
                            books = i.text
                            books = (books.replace("BOOKS", "")
                                     ).replace("\n", " ")
                            data['books'] = books
                        else:
                            data['books'] = "null"

                        if "APPS AND GAMES" in i.text:
                            app = i.text
                            app = (app.replace("APPS AND GAMES", "")
                                   ).replace("\n", " ")
                            data['app'] = app
                        else:
                            data['app'] = "null"

                        if "LIKES" in i.text:
                            likes = i.text
                            likes = (likes.replace("LIKES", "")
                                     ).replace("\n", " ")
                            data['likes'] = likes
                        else:
                            data['likes'] = "null"

                    backup_info = driver.find_element_by_id('viewport').text
                    backup_info = backup_info.replace("\n", " ")
                    data["backup_info"] = backup_info

                    infofile = name + ".json"

                    # os.chdir(folder+"/info")
                    with codecs.open(folder+'//info//'+infofile, 'w', encoding="utf-8") as out:
                        json.dump(data, out, indent=1, ensure_ascii=False)

                    stt += 1
                    with open(cachefile, 'w', encoding="utf-8") as out:
                        out.write(str(stt))
                except:
                    sleep(randint(3, 5))
                    continue
        driver.quit()
        # sleep(randint(90, 120))
    except NoSuchElementException:
        driver.quit()
        # sleep(randint(60, 90))
        continue
