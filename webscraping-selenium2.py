from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

"============================DEALING WITH MULTIPLE PAGES (CASE: AUDIBLE WEBSITE)============================"
options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("detach", True)

audible = 'https://www.audible.com/search'
path = '/Users/putriromhadhoni/Documents/Learning/analytics_eng/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path = path, options= options)
driver.get(audible)

container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
lists = container.find_elements('xpath', '//li[contains(@class,"productListItem")]')

title = []
subtitle =[]
author = []
length = []
releasedate = []
language = []
rating = []

for list in lists:
    title.append(list.find_element('xpath', './/h3[contains(@class,"bc-heading")]').text)
    author.append(list.find_element('xpath', './/li[contains(@class,"authorLabel")]').text)
    length.append(list.find_element('xpath', './/li[contains(@class,"runtimeLabel")]').text)
    releasedate.append(list.find_element('xpath', './/li[contains(@class,"releaseDateLabel")]').text)
    language.append(list.find_element('xpath', './/li[contains(@class,"languageLabel")]').text)
    rating.append(list.find_element('xpath', './/li[contains(@class,"ratingsLabel")]').text)
df = pd.DataFrame({'title': title, 'author':author, 'runtime': length, 'release_date': releasedate, 'language': language, 'ratings': rating})
df.to_csv('audiobook1.csv')

driver.quit()