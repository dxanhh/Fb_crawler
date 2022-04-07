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

today = date.today()
d1 = today.strftime("%d/%m/%Y")

# Yesterday date
yesterday = today - timedelta(days = 1)
d2 = yesterday.strftime("%d/%m/%Y")

folder = r"C:/batfile/set up server/crawl facebook"
g = open('uid_tau_hoa_clean_test.txt', "r")
link1 = g.readlines()

#cache file
cachefile = folder+'/cache/cache_test.txt' 
h = open(cachefile, "r")
cache = h.readlines()
numb = cache[0]
stt = int(numb)
print(stt)

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
    tendangnhap.send_keys('0855112000')
    sleep(randint(1, 3))
    matkhau = a.find_element_by_id('pass')
    matkhau.send_keys('luongvuthien15102000') 
    sleep(randint(1, 3))
    break
dangnhap = table.find_element_by_class_name('_6ltg').click()
sleep(randint(3, 5))

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

# try:
placelive = driver.find_element_by_xpath("//div[@id='living']")
living = placelive.find_element_by_xpath("//header[@id='u_0_e_mD']").text
living = (living.replace("Current town/city","")).replace("\n"," ")
# except:
#     living = "null"

# try:
placelive = driver.find_element_by_xpath("//div[@id='living']")
hometown = placelive.find_element_by_xpath("//div[@id='u_0_d_Mt']").text
hometown = (living.replace("Home town","")).replace("\n"," ")
# except:
#     hometown = "null"
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
    os.remove(folder+"/linkpost/"+linkpost)
else:
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
        data['hometown']  = hometown
    except:
        data['hometown']  = "null"
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