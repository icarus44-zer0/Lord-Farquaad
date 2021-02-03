# Josh Poe 
# Chrome Version 88.0.4324.96 (Official Build) (x86_64)
# selenium 3.141.0
# https://pypi.org/project/selenium/
#
#
#
#

from pandas.core.frame import DataFrame
import requests
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


<<<<<<< HEAD
login = 'https://csus.joinhandshake.com/login'
url = 'https://csus.joinhandshake.com/employers/167000' 
=======
url = 'https://www.citrusheights.net/Directory.aspx' 

driver = webdriver.Chrome(executable_path = 'C://Users//icarus44_zer0//Documents//GitHub//Lord-Farquaad//chromedriver.exe')
>>>>>>> dbc63a0c3abd68c9bb5630ef72969a0b4bca0a06

browser = webdriver.Chrome(executable_path = '/Users/jp/Documents/GitHub/Lord Farquaad/chromedriver')

<<<<<<< HEAD
#Login Screen
browser.get(login)
xpath = '//*[@id="sso-name"]'
element = browser.find_element_by_xpath(xpath)
element.click()

#SSO Page
xpath ='//*[@id="username"]'
=======
xpath = '//*[@id="directory_filter"]/label/input'
element = browser.find_element_by_xpath(xpath)

xpath = '//*[@id="directory"]/tbody/tr[1]/td[1]/a'
>>>>>>> dbc63a0c3abd68c9bb5630ef72969a0b4bca0a06
element = browser.find_element_by_xpath(xpath)
element.click()

# USERNAME 
element.send_keys('jpoe@csus.edu' + Keys.TAB)

<<<<<<< HEAD
#PASSWORD
xpath ='//*[@id="password"]'
element = browser.find_element_by_xpath(xpath)
element.click()
element.send_keys('' + Keys.RETURN)

#DUO PUSH
time.sleep(10)


x = 167000
while x < 167001:
    url = 'https://csus.joinhandshake.com/employers/' + str(x)
    browser.get(url)
    compName_xpath = '//*[@id="skip-to-content"]'
    email_xpath = '//*[@id="skip-to-content"]'

    element = browser.find_element_by_xpath(compName_xpath).text
    df = pd.read_csv(element)
    x += 1


def Convert(string): 
    li = list(string.split(" ")) 
    return li 

# url = 'https://csus.joinhandshake.com/employers/167000'
# browser.get(url)
# xpath = '//*[@id="skip-to-content"]'
# element = browser.find_element_by_xpath(xpath)
# element.select
# time.sleep(10)
# print(element)


=======
element.click() 
>>>>>>> dbc63a0c3abd68c9bb5630ef72969a0b4bca0a06

# element.copy()

# print(element)
