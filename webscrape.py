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
god_names = browser.find_elements_by_class_name('details__name') #find the god name
god_titles = browser.find_elements_by_class_name('details__title') #find the god 'title'? Description?

OG_god_names = []
OG_god_titles = []
god_info = ['God Name', 'God Title']

for god in god_names: #for god in god_names
	OG_god_names.append((god.text).upper()) #god.text is the text from the site, not sure how to get around this

for title in god_titles: #for title in god_titles
	OG_god_titles.append(title.text) #title.text is the text from the site, not sure how to get around this

smite_gods_dictionary = dict(zip(OG_god_names, OG_god_titles))


with open('smite-gods.csv', 'w', newline='') as gods_csv:
	headers = ['GOD', 'TITLE']
	writer = csv.DictWriter(gods_csv, fieldnames=headers)
	writer.writeheader()
	for god, title in smite_gods_dictionary.items(): #for each god in the list
		writer.writerow({'GOD': god, 'TITLE': title}) #write the god name to a row


browser.quit() #closes browser