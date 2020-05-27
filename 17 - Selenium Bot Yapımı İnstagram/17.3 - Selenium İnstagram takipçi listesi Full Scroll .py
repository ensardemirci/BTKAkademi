from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import js_asset

class Insta:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/')
        time.sleep(2)



        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)

        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        self.browser.get(f'https://www.instagram.com/{self.username}')
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        totalcount = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').text.strip(' takipçi')
        totalcount = int(totalcount)

        dialog = self.browser.find_element_by_css_selector('div[role=dialog] ul')

        flist = dialog.find_elements_by_css_selector('li')
        action = webdriver.ActionChains(self.browser)
        dialog.click()
        while True:
            fcount = len(dialog.find_elements_by_css_selector('li'))

            if len(dialog.find_elements_by_css_selector('li')) == totalcount:
                flist = dialog.find_elements_by_css_selector('li')
                for user in flist:
                    link = user.find_element_by_css_selector('a').get_attribute('href')
                    print(link)
                break
            else:
                print(totalcount)
                print(fcount)
                action.send_keys_to_element(dialog,Keys.END).perform()

                time.sleep(1)












insta = Insta('','')
insta.signIn()
insta.getFollowers()