from bs4 import BeautifulSoup
import requests
import csv

urls = []
with open('woman_depr_url.txt', 'r') as file0:
    for line in file0:
        line = line.replace('\\', '/')
        line = line.strip()
        urls.append(line)
file0.close()

#print(urls[:5])
prefix = '<p class="card__comment">'
texts = []

# for i,url in enumerate(urls):
#     if i % 10 == 0:
#         print(f'{i}/591')
#     full_url = 'https://www.woman.ru' + url
#     r = requests.get(full_url)
#     soup = BeautifulSoup(r.text, "html.parser")
#     text_ = soup.find(class_="card__comment")
#     x = text_.text.replace(prefix, '')
#     texts.append(x)


with open('woman_depr_text.txt', 'a') as file:
    writer = csv.writer(file, lineterminator='\n')

    for i, url in enumerate(urls[480:]):
        if (i) % 10 == 0:
            print(f'{i+481}/591')
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
