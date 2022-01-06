#!/usr/bin/env python3

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox() #The browser driver used
browser.get('https://www.smitegame.com/gods/achilles') #the site attempting to be accessed


browser.implicitly_wait(10)

#Example: GodClass, GodPantheon, GodRange, GodStyle = Warrior, Greek, Melee, Physical
GodInfo = []

#So this accidently found a list of everything I wanted?
SmiteGodInfo = browser.find_elements(By.CLASS_NAME, 'meta__single')
SmiteGodName = browser.find_element(By.CSS_SELECTOR, 'h1').text
SmiteGodTitle = browser.find_element(By.CSS_SELECTOR, 'h4').text

for info in SmiteGodInfo:
	GodInfo.append(info.text)


#there is probably a better way to go about addeding two items to the front of a list, this is what I have for now.
GodInfo.insert(0,(SmiteGodTitle).upper()) #Add title to 'front' of list
GodInfo.insert(0,(SmiteGodName).upper()) #add name to 'front' of list


with open('all-smite-gods.csv', 'w+', newline='') as gods_csv:
	headers = ['GOD', 'TITLE', 'CLASS','PANTHEON','RANGE','TYPE']
	writer = csv.writer(gods_csv)
	writer.writerow(headers)
	writer.writerow(GodInfo)





browser.quit() #closes browser