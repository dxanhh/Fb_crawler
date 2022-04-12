import time

from base import BaseClass
from datetime import date, timedelta
from push_to_mongodb import *
from selenium import webdriver

from resources.clone_acc import clone_acc
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from profile_extractor import ProfileExtractor
from time import sleep
import random



# INITIALIZE
today = date.today()
d1 = today.strftime("%d/%m/%Y")
yesterday = today - timedelta(days=1)
d2 = yesterday.strftime("%d/%m/%Y")
folder = r"resources/crawled_data"


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
            self.log.info("Initialize Chrome Driver")
            self.driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)
            self.facebook_login()

        except BaseException as e:
            self.log.critical(e)
            self.log.info('Initialize failed, aborting')
            self.driver.quit()

    def facebook_login(self):
        self.log.info('Tring to login')
        _email, _password = "0855112000", "luongvuthien15102000" #random.choice(list(clone_acc.items()))
        self.driver.get('http://mbasic.facebook.com')
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is('Facebook – log in or sign up'))
            email = self.driver.find_element(by=By.NAME, value='email')
            pw = self.driver.find_element(by=By.NAME, value='pass')
            email.send_keys(_email)
            pw.send_keys(_password)
            email.submit()
            self.log.info('Credentials sent')
            time.sleep(20)

            # return self.driver
        except TimeoutException:
            self.log.critical('Timeout: No login page found')

    def random_like(self):
        pass

    def _scroll(self):
        pages = random.randint(1, 5)
        total_scrolled = 0
        window_inner_height = self.driver.execute_script("return window.innerHeight;")
        self.log.info(f"Scrolling to {pages} page(s)")
        for _ in range(pages):
            random_slide = random.randint(3, 8)
            for i in range(random_slide):
                sleep(random.uniform(1, 5))
                scroll_to = random.uniform(100, 800)
                total_scrolled += scroll_to
                self.driver.execute_script(f"window.scrollBy(0,{scroll_to})")
                sleep(random.uniform(1, 5))
            try:
                to_scroll = window_inner_height - total_scrolled
                if to_scroll > 0:
                    self.driver.execute_script(f"window.scrollBy(0,{to_scroll + random.uniform(10, 100)})")
                element = self.driver.find_element(by=By.XPATH, value="//*[contains(text(), 'See more stories')]")
                self.log.info('Moving to new newfeed page')
                sleep(random.uniform(1, 5))
                self.driver.execute_script("arguments[0].click();", element)
            except NoSuchElementException as e:
                self.log.info("End of new feed reached")
                self.driver.quit()
                self.log.error(e)

            self.log.info("Finished scrolling")
        sleep(random.uniform(1.5, 4.5))

    def check_block(self):
        pass

    def _extract_info(self):
        self.log.info('Getting info')
        uid = get_one_uid() #"100076071382883"  # '100001155748489'
        try:
            url = f'https://mbasic.facebook.com/{str(uid)}' #f'https://m.facebook.com/{str(uid)}/about'
            self.log.info(f"Getting data from {url}")
            self.driver.get(url)
            page_source = (self.driver.page_source).encode('utf-8')
            data = ProfileExtractor(html=page_source, user_id=uid).extract()
            try:
                self.log.info("Pusing data to database...")
                push_one_user_profile(uid, data)
                self.log.info("Profile successfully inserted")
            except BaseException as e:
                self.log.error(f"Pushing failed {e}")
                push_one_uid(uid)

        except BaseException as e:
            self.log.error("failed", e)
            self.log.info(f"Pushing failed item with id: {uid} to database....")

            try:
                push_one_uid(uid)
                self.log.info("Successfully inserted failed data")
            except BaseException as e:
                self.log.error("Inserting failed", e)
                self.log.info(f"Pushing failed item with id: {uid} to database....")


        sleep(random.uniform(3, 5))
        self.driver.execute_script("window.history.go(-1)")

    def crawl(self):
        for actions in range(0, 20):
            self.log.info('Looped ' + str(actions) + ' time(s)')
            action = random.randint(1, 3)
            self.log.info(action)
            if action == 1:
                self.log.info('Scrolling')
                self._scroll()
            if action == 2:
                try:
                    self.log.info("Extracting info")
                    self._extract_info()
                except BaseException:
                    self.driver.quit()
            if action == 3:
                self.log.info('Sleeping')
                sleep(random.uniform(10, 15))
                self._extract_info()
        self.driver.quit()
        sleep(random.uniform(45, 90))

def main():
    crawler = FacebookCrawler(headless=False)
    crawler.crawl()

if __name__ == '__main__':
    main()
