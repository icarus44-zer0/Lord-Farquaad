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


url = 'https://www.energy.ca.gov/contact/commissioners-offices-and-divisions-contacts/staff-directory' 

driver = webdriver.Chrome(executable_path = '/Lord Farquaad/chromedriver')

browser = webdriver.Chrome()
browser.get(url)

xpath = '//*[@id="directory"]/tbody/tr[1]/td[1]/a'

element = browser.find_element_by_xpath(xpath)

element.click()


