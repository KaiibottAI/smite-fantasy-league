#!/usr/bin/env python3

import re
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as FireFoxOptions

url = 'https://www.smitegame.com/gods/'

#create the csv for the Smite Gods and their attributes
with open('all-smite-gods.csv', 'w+', newline='') as gods_csv:
	headers = ['GOD', 'TITLE', 'CLASS','PANTHEON','RANGE','TYPE']
	writer = csv.writer(gods_csv)
	writer.writerow(headers)


#Set the options to have Firefox in 'headless' mode
FireFoxOptions = FireFoxOptions()
FireFoxOptions.headless = True

try:
	#Opent the front page for the Smite Gods
	browser = webdriver.Firefox(options = FireFoxOptions)
	browser.get(url)
	browser.implicitly_wait(10)


	#Scrape the page for the links to the gods and make a list to open them later
	SmiteGodPages = browser.find_elements(By.CLASS_NAME, 'single__god')
	GodPages = [page.get_attribute('href') for page in SmiteGodPages]

	#iterate thru the links grabbed from the Smite Gods front page
	for page in GodPages:
		try:
			browser.get(page)
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

			with open('all-smite-gods.csv', 'a', newline='') as gods_csv:
				writer = csv.writer(gods_csv)
				writer.writerow(GodInfo)

		except ValueError:
			print(f"Well that didn't work")
except ValueError:
	print(f"Couldn't open {url} .")

#closes browser
browser.quit() 

print(f"Finished grabbing Smite God info!")