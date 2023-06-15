from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

### 1 part

# driver = webdriver.Chrome()
# driver.get("https://www.woman.ru/search/?q=%D0%B1%D0%B8%D0%BF%D0%BE%D0%BB%D1%8F%D1%80%D0%BD%D0%BE%D0%B5&where=forum_threads&sort=relevance&category=&control_charset=0")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# time.sleep(180)
#
# page_source = driver.page_source
#
# driver.quit()
#
# soup = BeautifulSoup(page_source, "html.parser")
#
# links = soup.findAll('div', class_="card")
#
# data = []
# for link in links:
#     x = link.find('a', class_="card__title-link text_carbon").get('href')
#     data.append(x)
#
# #print(data)
#
# with open('bar_url.txt', 'w') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     for elem in data:
#         writer.writerow([elem])
# file.close()

### 2 part

urls = []
with open('bar_url.txt', 'r') as file0:
    for line in file0:
        line = line.replace('\\', '/')
        line = line.strip()
        urls.append(line)
file0.close()
len_urls = len(urls)

prefix = '<p class="card__comment">'
texts = []

with open('bar_text.txt', 'a') as file:
    writer = csv.writer(file, lineterminator='\n')

    for i, url in enumerate(urls):
        if i % 10 == 0:
            print(f'{i}/{len_urls}')
        full_url = 'https://www.woman.ru' + url
        r = requests.get(full_url)
        soup = BeautifulSoup(r.text, "html.parser")
        text_ = soup.find(class_="card__comment")
        x = text_.text.replace(prefix, '')

        try:
            writer.writerow([x])
        except Exception:
            print(url)

    # for elem in texts:
    #     writer.writerow([elem])
file.close()