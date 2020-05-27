from selenium import webdriver
import time

driver = webdriver.Firefox()

url = 'https://youtubeabonem.com'

driver.get(url)

time.sleep(2)
driver.maximize_window()
print(driver.title)

time.sleep(2)

driver.close()