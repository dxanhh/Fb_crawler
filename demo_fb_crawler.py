from base import BaseClass
from datetime import date, timedelta

from selenium import webdriver
from resources.clone_acc import clone_acc
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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
    def __init__(self, headless: bool =True):
        super().__init__()
        try:
            options = Options()
            self.log.info("Setting headless options")
            options.headless = headless
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("detach", True)
            # desired_cap = {
            #     "deviceName": "iPhone X"
            # }
            # options.add_experimental_option('mobileEmulation', desired_cap)

            self.log.info("Initialize Chrome Driver")
            self.driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)
            self.facebook_login()
        except BaseException as e:
            self.log.critical(e)
            self.log.info('Initialize failed, aborting')

    def facebook_login(self):
        self._email, self._password = 'frost.wyrm318@gmail.com', 'abcxyz'#random.choice(list(clone_acc.items()))
        self.driver.get('http://facebook.com')
        try:
            WebDriverWait(self.driver, 30).until(EC.title_is('Facebook – log in or sign up'))
            email = self.driver.find_element(by=By.NAME, value='email')
            pas = self.driver.find_element(by=By.NAME, value='pass')
            email.send_keys(self._email)
            pas.send_keys(self._password)
            email.submit()
            return self.driver
        except TimeoutException:
            self.log.critical('Timeout: No login page found')

    # def _check_login(self) -> bool:
    #     selector_to_homepage = '#mount_0_0_7P > div > div:nth-child(1) > div > div:nth-child(4) > div.ehxjyohh.kr520xx4.poy2od1o.b3onmgus.hv4rvrfc.n7fi1qx3 > div.du4w35lb.l9j0dhe7.byvelhso.rl25f0pe.j83agx80.bp9cbjyn'
    #     try:
    #         element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, selector_to_homepage)))
    #         element.click()
    #         if element:
    #             return True
    #     except TimeoutException as e:
    #         self.log.critical(e)
    #         return False

    def _scroll(self):
        scroll = random.randint(0, 5)
        for i in range(scroll, 10):
            sleep(random.randint(1, 5))
            scroll += 1
            scroll1 = random.randint(100, 800)
            self.driver.execute_script(
                "window.scrollBy(0,{})".format(scroll1), "")


    def _view_story(self):
        sleep(random.randint(7, 10))
        self.log.info("Sleeping")
        self.driver.get('https://m.facebook.com/')
        try:
            sleep(5)
            story = self.driver.find_element(by=By.XPATH("//div[@class='_6m42 nineBySixteen']"))
            story.click()
            sleep(random.randint(2, 3))
            close = self.driver.find_element(by=By.XPATH("//i[@data-sigil='m-stories-close-story-button']"))
            close.click()
        except:
            return False

    def _extract_info(self):
        self.log.info('Getting info')
        data = {}
        try:
            self.driver.get('https://m.facebook.com/' + str(link1[stt]))

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
            with codecs.open(folder + '//info//' + infofile, 'w', encoding="utf-8") as out:
                json.dump(data, out, indent=1, ensure_ascii=False)

            stt += 1
            with open(cachefile, 'w', encoding="utf-8") as out:
                out.write(str(stt))
        except:
            sleep(randint(3, 5))
            continue

    def crawl(self):
        for actions in range(0, 20):
            self.log.info('Looped' + str(actions) + 'times')
            action = random.randint(1, 3)
            if action == 1:
               self._scroll()
            if action == 2:
                action = self._view_story()
                if not action:
                    continue
            if action == 3:
                self._extract_info()
        driver.quit()
        # sleep(randint(90, 120))
    except NoSuchElementException:
        driver.quit()
        # sleep(randint(60, 90))
        continue

def main():
    # stt = int(read_checkpoint())
    # print(stt)

    crawler = FacebookCrawler(headless=False)
    crawler.facebook_login()
    print(crawler._check_login())



if __name__ == '__main__':
    main()
