from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

"============================DEALING WITH MULTIPLE PAGES (CASE: AUDIBLE WEBSITE)============================"
options = webdriver.ChromeOptions()
#options.headless = True
options.add_experimental_option("detach", True)

audible = 'https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=8a113f1a-dc38-418d-b671-3cca04245da5&pf_rd_r=CYS6Y53ND5ZQ8A1E3NNQ&pageLoadId=7V2aV088KJUan721&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc'
#audible = 'https://www.audible.com/search'
path = '/Users/putriromhadhoni/Documents/Learning/analytics_eng/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path = path, options= options)
driver.get(audible)

#pagination
pagination = driver.find_elements('xpath', '//ul[contains(@class, "pagingElements")]/li')
#pages = pagination.find_elements('By.TAG_NAME', 'li')
last_page = int(pagination[-2].text) #find total pages 

#initial page
current_page = 1

title = []
subtitle =[]
author = []
length = []
releasedate = []
language = []
rating = []

#looping for pagination
while current_page <= last_page:
    time.sleep(5)
    container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
    lists = container.find_elements('xpath', '//li[contains(@class,"productListItem")]')

    for list in lists:
        title.append(list.find_element('xpath', './/h3[contains(@class,"bc-heading")]').text)
        author.append(list.find_element('xpath', './/li[contains(@class,"authorLabel")]').text)
        length.append(list.find_element('xpath', './/li[contains(@class,"runtimeLabel")]').text)
        releasedate.append(list.find_element('xpath', './/li[contains(@class,"releaseDateLabel")]').text)
        language.append(list.find_element('xpath', './/li[contains(@class,"languageLabel")]').text)
        rating.append(list.find_element('xpath', './/li[contains(@class,"ratingsLabel")]').text)    
    
    current_page = current_page + 1

    #click next page
    try:
        next_page = driver.find_element('xpath', './/span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

df = pd.DataFrame({'title': title, 'author':author, 'runtime': length, 'release_date': releasedate, 'language': language, 'ratings': rating})
print(df.shape)
print(last_page)
df.to_csv('bestseller.csv')
