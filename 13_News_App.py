import requests
import time
import os

unformatted_time = time.localtime()
formatted_time = time.strftime('%d/%m/%Y', unformatted_time)
print(formatted_time)

apikey = os.getenv("NewsAPI")

query = input("what type of news do you want to read: ")
url = f'https://newsapi.org/v2/everything?q={query}&language=en&from={formatted_time}&sortBy=publishedAt&apiKey={apikey}'

response = requests.get(url)
data = response.json()
# print(data)
for article in data['articles']:
    print(f"\nTitle: {article['title']}")
    print(f"Description: {article['description']}")
    print("______________________________________")

input('press ENTER to exit')