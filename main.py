import requests
import os

from send_email import send_email

api_key = os.getenv("API_KEY_NEWS")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-03-25&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

raw_message = ""
for article in content["articles"]:
    if article["title"] is not None:
        raw_message = raw_message + (article["title"]) + "\n"
    raw_message = raw_message + (article["description"]) + "\n"
    raw_message = raw_message + (article["url"]) + "\n\n"
# raw_message = raw_message.encode('utf-8')

message = f"""\
Subject: daily news

From: news API

{raw_message}
"""

send_email(message)
print(message)
