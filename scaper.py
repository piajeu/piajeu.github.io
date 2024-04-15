# Import package requests dan BeautifulSoup
import requests
from bs4 import BeautifulSoup
import datetime

# Requests ke website
page = requests.get("https://www.republika.co.id/")

# Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, 'html.parser')

# Buka file untuk ditulis
with open('scraping.txt', 'w', encoding='utf-8') as file:
    file.write('Judul\n')
    file.write('============================================\n')
    titles = obj.find_all('div', class_='title')
    for i, title in enumerate(titles, 1):
        file.write(f"{i}. {title.text.strip()}\n")

    file.write('\nKategori\n')
    file.write('============================================\n')
    categories = obj.find_all('span',class_='kanal-info')
    for category in categories:
        file.write(f"{category.text.strip()}\n")

    file.write('\nWaktu publish\n')
    file.write('============================================\n')
    publish_times = obj.find_all('div',class_='date')
    for publish_time in publish_times:
        file.write(f"{publish_time.text.strip()}\n")

    file.write('\nWaktu Scraping\n')
    file.write('============================================\n')
    current_time = datetime.datetime.now()
    file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

print("Data telah disimpan dalam file 'scraping.txt'")
