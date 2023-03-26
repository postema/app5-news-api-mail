import requests
import os

from send_email import send_email

api_key = os.getenv("API_KEY_NEWS")

subject = "daily news from API"
topic = "gold"

url = f"https://newsapi.org/v2/everything?q={topic}&language=en&from=2023-03-25&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
response = request.json()

raw_message = f"Subject: {subject}" + "\n"
for article in response["articles"][:10]:
    if article["title"] is not None:
        raw_message = raw_message + (article["title"]) + "\n"
    raw_message = raw_message + (article["description"]) + "\n"
    raw_message = raw_message + (article["url"]) + "\n\n"
raw_message = raw_message.encode('utf-8')

send_email(raw_message)
print(raw_message)
