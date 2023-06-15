from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

driver = webdriver.Chrome()
driver.get("https://www.woman.ru/search/?q=%D0%B4%D0%B5%D0%BF%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F&where=forum")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(180)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, "html.parser")

#print(soup)

links = soup.findAll('div', class_="card")

data = []
for link in links:
    x = link.find('a', class_="card__title-link text_carbon").get('href')
    data.append(x)

#print(data)

with open('woman_depr.txt', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    for elem in data:
        writer.writerow([elem])
file.close()