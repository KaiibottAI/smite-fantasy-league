#!/usr/bin/env python3

import requests
import re
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox() #The browser driver used
browser.get('https://www.smitegame.com/gods/') #the site attempting to be accessed


time.sleep(2)#required for the page to load in time and then continue to scrape from page
print(browser.title) #grab the title of the page
SmiteGodNames = browser.find_elements_by_class_name('details__name') #find the god name
SmiteGodTitles = browser.find_elements_by_class_name('details__title') #find the god 'title'? Description?

GodNamesList = []
GodTitlesList = []

for god in SmiteGodNames: #for god in SmiteGodNames
	GodNamesList.append((god.text).upper()) #god.text is the text from the site, not sure how to get around this

for title in SmiteGodTitles: #for title in SmiteGodTitles
	GodTitlesList.append(title.text) #title.text is the text from the site, not sure how to get around this

smite_gods_dictionary = dict(zip(GodNamesList, GodTitlesList))


with open('smite-gods.csv', 'w', newline='') as gods_csv:
	headers = ['GOD', 'TITLE']
	writer = csv.DictWriter(gods_csv, fieldnames=headers)
	writer.writeheader()
	for god, title in smite_gods_dictionary.items(): #for each god in the list
		writer.writerow({'GOD': god, 'TITLE': title}) #write the god name to a row


browser.quit() #closes browser