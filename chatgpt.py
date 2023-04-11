from selenium import webdriver 
import time 

driver = webdriver.Chrome('/Users/putriromhadhoni/Documents/Learning/analytics_eng/chromedriver/chromedriver') 
driver.get("https://www.amazon.com/s?k=self+help+book&ref=nb_sb_noss") 
time.sleep(5)

spans = driver.find_elements_by_xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']")
for span in spans:
    print(span.text)

driver.quit()