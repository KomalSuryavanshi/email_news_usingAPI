import requests

api_key = "c6b429d9175945719e113cda6d6c5ff3"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-03-03&" \
      "sortBy=publishedAt&apiKey=c6b429d9175945719e113cda6d6c5ff3"

# Make request
request = requests.get(url)

# Get a dictionary with data
# content = request.text  ---> This give the content in the form of str but we need a dictionary type
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"], "->", article["description"])

