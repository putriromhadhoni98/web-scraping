### WEB SCRAPING USING BEAUTIFUL SOUP ###

import requests
import bs4
import lxml
import pandas as pd

#SCRAPING BOOK'S INFORMATION FROM http://books.toscrape.com/catalogue/page-1.html

req = requests.get("http://books.toscrape.com/catalogue/page-{}.html".format('1'))
soup = bs4.BeautifulSoup(req.text, "html.parser")
product_pod = soup.select(".product_pod")

#list the title of book
title = []
for i in range(50):
    req = requests.get("http://books.toscrape.com/catalogue/page-{}.html".format(i+1))
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    product_pod = soup.select(".product_pod")
    for i in range(20):
        title.append(product_pod[i]('a')[1]['title'])

title

#list the price of the book
price = []
for i in range(50):
    req = requests.get("http://books.toscrape.com/catalogue/page-{}.html".format(i+1))
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    product_pod = soup.select(".product_pod")
    for i in range(20):
        price.append(product_pod[i]("div")[1].get_text()[2:8])

price

#list the rating of the book
rating = []
for i in range(50):
    req = requests.get("http://books.toscrape.com/catalogue/page-{}.html".format(i+1))
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    product_pod = soup.select(".product_pod")
    for i in range(20):
        rating.append(product_pod[i]("p")[0]["class"][1])

rating

#create DataFrame
book_info = pd.DataFrame(
        {"No" : [i for i in range(1,1001)],
        "Title" : title,
        "Price" : price,
        "Rating" : rating
                })

#replacing the values of rating column by numeric
book_info['Rating'].replace("One", 1, inplace = True)
book_info['Rating'].replace("Two", 2, inplace = True)
book_info['Rating'].replace("Three", 3, inplace = True)
book_info['Rating'].replace("Four", 4, inplace = True)
book_info['Rating'].replace("Five", 5, inplace = True)  

print('testing')
print('halo ini hanya testing')
  