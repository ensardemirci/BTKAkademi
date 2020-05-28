from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class YTAbonem:
    def __init__(self,username,password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://youtubeabonem.com')
        time.sleep(1)

        self.browser.maximize_window()
        time.sleep(1)

        self.browser.find_element_by_xpath('//*[@id="header"]/div/nav/ul/li[7]/a').click()
        time.sleep(1)


        self.browser.find_element_by_xpath('//*[@id="sorgusonucla"]/div/div/div/div/div[2]/form/div[1]/div/input').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="sorgusonucla"]/div/div/div/div/div[2]/form/div[2]/div/input').send_keys(self.password)

        for i in range(70,0,-1):
            time.sleep(1)
            print(i)

        self.browser.find_element_by_xpath('//*[@id="sorgusonucla"]/div/div/div/div/div[2]/form/button').click()
        time.sleep(1)

    def getPoints(self):
        act = webdriver.ActionChains(self.browser)
        self.browser.get('https://youtubeabonem.com/?page=module&md=youtube4k')
        time.sleep(1)
        if self.browser.find_element_by_class_name('visit_button'):
            i = 0
            while i < 10:
                self.browser.find_element_by_class_name('visit_button').click()
                time.sleep(2)
                self.browser.find_element_by_id('ytPlayer').click()
                time.sleep(2)
                act.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
                time.sleep(1)
                self.browser.get('https://youtubeabonem.com/?page=module&md=youtube4k')
                i = i + 1
                time.sleep(2)
            time.sleep(200)
            a = 0
            while a < 10:
                act.key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()
                time.sleep(1)
                a = a + 1
        else:
            yt.getPoints()
yt = YTAbonem('keyifli99', '123qwe123')
yt.signIn()
while True:
    yt.getPoints()
