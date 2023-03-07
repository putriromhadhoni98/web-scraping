from bs4 import BeautifulSoup
import requests
import os.path

'''
Steps:
1. Fetch the pages
result = requests.get("url")
2. Page content
content = result.text
3. create soup
soup = BeautifulSoup(content, 'lxml')

Finding Element
soup.find(id = "specific id")
soup.find('tag', class = class_name)
soup.find/soup.find_all('h1')
'''

# website = "https://subslikescript.com/movie/Titanic-120338"
# result = requests.get(website)
# soup = BeautifulSoup(result.text, 'lxml')

# box = soup.find('article', class_ = 'main-article')
# title = box.find('h1').get_text()
# transkrip = box.find('div', class_ = 'full-script').get_text(strip = True, separator = ' ')

# with open(f'{title}.txt', 'w') as file:
#     file.write(transkrip)

root = "https://subslikescript.com"
web = f'{root}/movies'
res = requests.get(web)
soup1 = BeautifulSoup(res.text, 'lxml')

#MULTIPLE LINK

box1 = soup1.find('article', class_ = 'main-article')
links = []
for link in box1.find_all('a', href = True):
    links.append(link['href'])
# print(links)

path = '/Users/putriromhadhoni/Documents/Learning/analytics_eng/web-scraping-res'

for link in links:
    web1 = f'{root}/{link}'
    ress = requests.get(web1)
    soup2 = BeautifulSoup(ress.text, 'lxml')

    box = soup2.find('article', class_ = 'main-article')
    title = box.find('h1').get_text()
    transkrip = box.find('div', class_ = 'full-script').get_text(strip = True, separator = ' ')

    # with open(os.path.join(path, f'{title}.txt'), 'w') as file:
    #     file.write(transkrip)

#pagination

