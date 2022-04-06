from base import BaseClass
from datetime import date, timedelta

from selenium import webdriver
from resources.clone_acc import clone_acc
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from time import sleep
import os.path
import random
import os
import codecs
import json

# https://github.dev/SkullTech/friends-scraper/blob/master/scrapefriends.py


# INITIALIZE
today = date.today()
d1 = today.strftime("%d/%m/%Y")
yesterday = today - timedelta(days=1)
d2 = yesterday.strftime("%d/%m/%Y")
folder = r"resources/crawled_data"



def get_uid():
    """Get facebook user id
    :return: the list of facebook user ID
    """
    g = open('resources/user_id.txt', "r")
    return g.readlines()


def read_checkpoint():
    """Read current crawler checkpoint
    :return: the last value in the checkpoint
    """

    cachefile = "resources/checkpoint/6_4.txt"
    h = open(cachefile, "r")
    cache = h.readlines()
    return cache[0]

class FacebookCrawler(BaseClass):
    def __init__(self, headless=True):
        super().__init__()
        try:
            options = Options()
            self.log.info("Setting headless options")
            options.headless = headless
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("detach", True)
            self.log.info("Initialize Chrome Driver")
            self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        except BaseException:
            self.log.info('Initialize failed, aborting')

    def facebook_login(self):
        self._email, self._password = random.choice(list(clone_acc.items()))
        self.driver.get('http://www.facebook.com')
        try:
            WebDriverWait(self.driver, 30).until(EC.title_is('Facebook – log in or sign up'))
            email = self.driver.find_element_by_name('email')
            pas = self.driver.find_element_by_name('pass')
            email.send_keys(self._email)
            pas.send_keys(self._password)
            email.submit()
            return self.driver
        except TimeoutException:
            self.log.critical('Timeout: No login page found')

    def demo(self):
        for loop in range(0, 1000):
            try:
                self.log.info('Logging into Facebook')
                self.driver.get('https://www.facebook.com/')
                self.driver.maximize_window()
                sleep(0)

            except BaseException:
                pass


        #         table = driver.find_element_by_class_name('_9vtf')
        #         rows = table.find_elements_by_tag_name('div')
        #
        #         account = randint(0, len(list_tk_clone)-1)
        #         account = 3
        #
        #         for a in rows:
        #             tendangnhap = a.find_element_by_id('email')
        #             tendangnhap.send_keys(list_tk_clone[account])
        #             sleep(randint(1, 3))
        #             matkhau = a.find_element_by_id('pass')
        #             matkhau.send_keys(list_mk_clone[account])
        #             sleep(randint(1, 3))
        #             break
        #         dangnhap = table.find_element_by_class_name('_6ltg').click()
        #         sleep(randint(3, 5))
        #
        #         for actions in range(0, 20):
        #             print('vong lap thu: ' + str(actions))
        #             # action = randint(1, 3)
        #             action = 3
        #             # giả vờ lướt newfeed để facebook không chặn
        #             if action == 1:
        #                 driver.get('https://m.facebook.com/')
        #                 print('luot newfeed')
        #                 # luot_new_feed
        #                 scroll = randint(0, 5)
        #                 for i in range(scroll, 10):
        #                     sleep(randint(1, 5))
        #                     scroll += 1
        #                     scroll1 = randint(100, 800)
        #                     driver.execute_script(
        #                         "window.scrollBy(0,{})".format(scroll1), "")
        #             if action == 2:
        #                 sleep(randint(7, 10))
        #                 print("sleeping")
        #                 # #click_story
        #                 # driver.get('https://m.facebook.com/')
        #                 # try:
        #                 #     sleep(5)
        #                 #     story = driver.find_element_by_xpath("//div[@class='_6m42 nineBySixteen']")
        #                 #     story.click()
        #                 #     sleep(randint(2, 3))
        #                 #     close = driver.find_element_by_xpath("//i[@data-sigil='m-stories-close-story-button']").click()
        #                 # except:
        #                 #     continue
        #             if action == 3:
        #                 print('laythongtin')
        #
        #                 data = {}
        #
        #                 try:
        #                     driver.get('https://m.facebook.com/'+str(link1[stt]))
        #
        #                     data["UID"] = str(link1[stt].replace("\n", ""))
        #
        #                     sleep(randint(3, 5))
        #                     # lấy thông tin cá nhân
        #
        #                     info = driver.find_element_by_xpath("//div[@id='profile_intro_card']").click()
        #                     sleep(randint(3, 5))
        #
        #                     name = driver.find_element_by_class_name('_6j_c').text
        #
        #                     print(name)
        #
        #                     data['name'] = name
        #
        #                     if "blocked" in name:
        #                         break
        #                         list_tk_clone.pop(account)
        #                         list_mk_clone.pop(account)
        #                         driver.quit()
        #
        #                     if "moment" in name:
        #                         break
        #                         list_tk_clone.pop(account)
        #                         list_mk_clone.pop(account)
        #                         driver.quit()
        #
        #                     scroll = randint(0, 5)
        #
        #                     for i in range(scroll, 10):
        #                         sleep(randint(1, 3))
        #                         scroll1 = randint(300, 800)
        #                         driver.execute_script(
        #                             "window.scrollBy(0,{})".format(scroll1), "")
        #
        #                     driver.execute_script("window.scrollTo(0,0)", "")
        #
        #                     try:
        #                         edu = driver.find_element_by_xpath(
        #                             "//div[@id='education']").text
        #                         edu = (edu.replace("EDUCATION", "")).replace("\n", " ")
        #                         data['education'] = edu
        #                     except:
        #                         data['education'] = 'null'
        #
        #                     try:
        #                         work = driver.find_element_by_xpath(
        #                             "//div[@id='work']").text
        #                         work = (work.replace("WORK", "")).replace("\n", " ")
        #                         data['work'] = work
        #                     except:
        #                         data['work'] = "null"
        #
        #                     try:
        #                         living = driver.find_element_by_xpath(
        #                             "//div[@id='living']").text
        #                         living = (living.replace("PLACES LIVED", "")
        #                                   ).replace("\n", " ")
        #                         data['placelive'] = living
        #                     except:
        #                         data['placelive'] = "null"
        #
        #                     try:
        #                         contact_info = driver.find_element_by_xpath(
        #                             "//div[@id='contact-info']").text
        #                         contact_info = (contact_info.replace(
        #                             "CONTACT INFO", "")).replace("\n", " ")
        #                         data['contact_info'] = contact_info
        #                     except:
        #                         data['contact_info'] = "null"
        #
        #                     try:
        #                         basic_info = driver.find_element_by_xpath(
        #                             "//div[@id='basic-info']").text
        #                         basic_info = (basic_info.replace(
        #                             "BASIC INFO", "")).replace("\n", " ")
        #                         data['basic_info'] = basic_info
        #                     except:
        #                         data['basic_info'] = "null"
        #
        #                     try:
        #                         relationship = driver.find_element_by_xpath(
        #                             "//div[@id='relationship']").text
        #                         relationship = (relationship.replace(
        #                             "RELATIONSHIP", "")).replace("\n", " ")
        #                         data['relationship'] = relationship
        #                     except:
        #                         data['relationship'] = "null"
        #
        #                     try:
        #                         bio = driver.find_element_by_xpath(
        #                             "//div[@id='bio']").text
        #                         bio = (bio.replace("BIO", "")).replace("\n", " ")
        #                         data['bio'] = bio
        #                     except:
        #                         data['bio'] = "null"
        #
        #                     tonghop = driver.find_elements_by_xpath(
        #                         "//div[@class='_55wo _2xfb _1kk1']")
        #
        #                     for i in tonghop:
        #                         if "CHECK-INS" in i.text:
        #                             checkin = i.text
        #                             checkin = (checkin.replace(
        #                                 "CHECK-INS", "")).replace("\n", " ")
        #                             data['checkin'] = checkin
        #                         else:
        #                             data['checkin'] = "null"
        #
        #                         if "SPORTS" in i.text:
        #                             sport = i.text
        #                             sport = (sport.replace("CHECK-INS", "")
        #                                      ).replace("\n", " ")
        #                             data['sport'] = sport
        #                         else:
        #                             data['sport'] = "null"
        #
        #                         if "MUSIC" in i.text:
        #                             music = i.text
        #                             music = (music.replace("MUSIC", "")
        #                                      ).replace("\n", " ")
        #                             data['music'] = music
        #                         else:
        #                             data['music'] = "null"
        #
        #                         if "FILMS" in i.text:
        #                             films = i.text
        #                             films = (films.replace("FILMS", "")
        #                                      ).replace("\n", " ")
        #                             data['films'] = films
        #                         else:
        #                             data['films'] = "null"
        #
        #                         if "TV PROGRAMMES" in i.text:
        #                             tv = i.text
        #                             tv = (tv.replace("TV PROGRAMMES", "")
        #                                   ).replace("\n", " ")
        #                             data['television'] = tv
        #                         else:
        #                             data['television'] = "null"
        #
        #                         if "BOOKS" in i.text:
        #                             books = i.text
        #                             books = (books.replace("BOOKS", "")
        #                                      ).replace("\n", " ")
        #                             data['books'] = books
        #                         else:
        #                             data['books'] = "null"
        #
        #                         if "APPS AND GAMES" in i.text:
        #                             app = i.text
        #                             app = (app.replace("APPS AND GAMES", "")
        #                                    ).replace("\n", " ")
        #                             data['app'] = app
        #                         else:
        #                             data['app'] = "null"
        #
        #                         if "LIKES" in i.text:
        #                             likes = i.text
        #                             likes = (likes.replace("LIKES", "")
        #                                      ).replace("\n", " ")
        #                             data['likes'] = likes
        #                         else:
        #                             data['likes'] = "null"
        #
        #                     backup_info = driver.find_element_by_id('viewport').text
        #                     backup_info = backup_info.replace("\n", " ")
        #                     data["backup_info"] = backup_info
        #
        #                     infofile = name + ".json"
        #
        #                     # os.chdir(folder+"/info")
        #                     with codecs.open(folder+'//info//'+infofile, 'w', encoding="utf-8") as out:
        #                         json.dump(data, out, indent=1, ensure_ascii=False)
        #
        #                     stt += 1
        #                     with open(cachefile, 'w', encoding="utf-8") as out:
        #                         out.write(str(stt))
        #                 except:
        #                     sleep(randint(3, 5))
        #                     continue
        #         driver.quit()
        #         # sleep(randint(90, 120))
        #     except NoSuchElementException:
        #         driver.quit()
        #         # sleep(randint(60, 90))
        #         continue

def main():
    # stt = int(read_checkpoint())
    # print(stt)

    crawler = FacebookCrawler(headless=False)
    crawler.facebook_login()



if __name__ == '__main__':
    main()
