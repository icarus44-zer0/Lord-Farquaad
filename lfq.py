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


login = 'https://csus.joinhandshake.com/login'
url = 'https://csus.joinhandshake.com/employers/167000' 

browser = webdriver.Chrome(executable_path = '/Users/jp/Documents/GitHub/Lord Farquaad/chromedriver')

#Login Screen
browser.get(login)
xpath = '//*[@id="sso-name"]'
element = browser.find_element_by_xpath(xpath)
element.click()

#SSO Page
xpath ='//*[@id="username"]'
element = browser.find_element_by_xpath(xpath)
element.click()

# USERNAME 
element.send_keys('jpoe@csus.edu' + Keys.TAB)

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




