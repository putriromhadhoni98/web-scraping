from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


"============================SCRAPE DATA FROM A TABLE============================"

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/putriromhadhoni/Documents/Learning/analytics_eng/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path = path, options= options)
driver.get(website)

'''
Finding element in selenium:
driver.find_element_by_id("id")
driver.find_element_by_class_name("class_name")
driver.find_element_by_tag_name("tag")
driver.find_element_by_xpath("//tag@AttributeName="value"]")
driver.find_element_by_css_selector()
driver.find_element_by_name()
driver.find_element_by_link_text()
multiple elements -> replace element with elements
'''
#dropdown menu
dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('France')
time.sleep(3)

#click
all_matches = driver.find_element('xpath','//label[@analytics-event="All matches"]')
all_matches.click()

#Extracting data from table
matches = driver.find_elements(By.TAG_NAME, 'tr')
date = []
home = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element('xpath', './td[1]').text)
    home.append(match.find_element('xpath', './td[2]').text)
    score.append(match.find_element('xpath', './td[3]').text)
    away_team.append(match.find_element('xpath', './td[4]').text)

df = pd.DataFrame({'date': date, 'home': home, 'score' : score, 'away_team': away_team})
print(df.shape)
df.to_csv('result.csv')
