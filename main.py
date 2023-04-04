import requests
from send_email import send_email

topic = "apple"
api_key = "c6b429d9175945719e113cda6d6c5ff3"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-03&" \
      "sortBy=publishedAt&" \
      "apiKey=c6b429d9175945719e113cda6d6c5ff3&" \
      "language=en"                              # language en will show only english news

# Make request
request = requests.get(url)

# Get a dictionary with data
# content = request.text  ---> This give the content in the form of str but we need a dictionary type
content = request.json()

# Access the article titles and descriptions
email_news = ""
for article in content["articles"][:10]:              # [:10] will give only 10 news
    email_news = email_news + article["title"] + "\n" \
                 + article["description"] + 2*"\n" + "\n" \
                 + article["url"]

news_content = f"""\
Subject: Today's news
{email_news}
        """
news_content = news_content.encode("utf-8")
send_email(message=news_content)




