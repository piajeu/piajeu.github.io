import json

# Baca file JSON
with open('json.json', 'r') as file: 
    data = json.load(file)

# Ekstraksi data dari file JSON
articles = data["articles"]
categories = data["categories"]
publish_times = data["publish_times"]
scraping_time = data["scraping_time"]

# Tampilkan hasil ekstraksi
print("Articles:")
for article in articles:
    print(article)

print("\nCategories:")
for category in categories:
    print(category)

print("\nPublish Times:")
for publish_time in publish_times:
    print(publish_time)

print("\nScraping Time:")
print(scraping_time)
