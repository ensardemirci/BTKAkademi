from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class YTTakipkazan:
    def __init__(self,username,password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://takipkazan.com')
        time.sleep(1)

        self.browser.maximize_window()
        time.sleep(1)

        self.browser.find_element_by_xpath('/html/body/header/div/div[2]/form/input[1]').send_keys(self.username)
        self.browser.find_element_by_xpath('/html/body/header/div/div[2]/form/input[2]').send_keys(self.password)
        self.browser.find_element_by_xpath('/html/body/header/div/div[2]/form/input[3]').click()
        time.sleep(5)

    def getPoints(self):
        act = webdriver.ActionChains(self.browser)
        ilk = ''
        while True:
            self.browser.get('https://takipkazan.com/p.php?p=youtube')
            time.sleep(5)
            if self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/center/div/center/a'):
                self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/center/div/center/a').click()
                if self.browser.find_element_by_id('ytPlayer'):
                    self.browser.find_element_by_id('ytPlayer').click()
                    son = self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/center/a[1]').get_attribute('href')
                    print('ilk',ilk)
                    print('son',son)

                    if ilk == son:
                        self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/center/a[1]').click()
                    else:
                        time.sleep(30)
                        ilk = son

                else:
                    continue
            else:
                continue

yt = YTTakipkazan('hgh2828hgh', '123qwe123')
yt.signIn()
yt.getPoints()
