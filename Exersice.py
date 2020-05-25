from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class YT:
    def __init__(self,username,password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/')
        time.sleep(2)



        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(Keys.ENTER)



yt = YT('hugegamerhobbit','1806ens9393')
yt.signIn()