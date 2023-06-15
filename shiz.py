from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import re

### 1 part

# driver = webdriver.Chrome()
# driver.get("https://www.woman.ru/search/?q=%D1%88%D0%B8%D0%B7%D0%BE%D1%84%D1%80%D0%B5%D0%BD%D0%B8%D1%8F&where=forum_threads&sort=relevance&control_charset=0&category=")
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
# with open('shiz_url.txt', 'w') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     for elem in data:
#         writer.writerow([elem])
# file.close()

### 2 part

urls = []
with open('shiz_url.txt', 'r') as file0:
    for line in file0:
        line = line.replace('\\', '/')
        line = line.strip()
        urls.append(line)
file0.close()
len_urls = len(urls)

prefix = '<p class="card__comment">'
texts = []

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

with open('shiz_text.txt', 'a') as file:
    writer = csv.writer(file, lineterminator='\n')

    for i, url in enumerate(urls[255:]):
        if (255+i) % 10 == 0:
            print(f'{i}/{len_urls}')
        full_url = 'https://www.woman.ru' + url
        r = requests.get(full_url)
        soup = BeautifulSoup(r.text, "html.parser")
        text_ = soup.find(class_="card__comment")
        x = text_.text.replace(prefix, '')

        x = emoji_pattern.sub(r'', x)

        try:
            writer.writerow([x])
        except Exception:
            print(url)

    # for elem in texts:
    #     writer.writerow([elem])
file.close()