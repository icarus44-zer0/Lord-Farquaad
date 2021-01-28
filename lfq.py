# Josh Poe 
# Chrome Version 88.0.4324.96 (Official Build) (x86_64)
# selenium 3.141.0
# https://pypi.org/project/selenium/
#
#
#
#



import requests
from selenium import webdriver


url = 'https://www.citrusheights.net/Directory.aspx' 

driver = webdriver.Chrome(executable_path = 'C://Users//icarus44_zer0//Documents//GitHub//Lord-Farquaad//chromedriver.exe')

browser = webdriver.Chrome()
browser.get(url)

xpath = '//*[@id="directory_filter"]/label/input'
element = browser.find_element_by_xpath(xpath)

xpath = '//*[@id="directory"]/tbody/tr[1]/td[1]/a'
element = browser.find_element_by_xpath(xpath)

element.click() 

# element.copy()

# print(element)
