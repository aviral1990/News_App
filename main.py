import requests

#url of newsapi.org
url="https://newsapi.org/v2/everything?q=tesla&from=2023-01-28&sortBy=publishedAt&apiKey=49c747a1260e447bba1b4a53c6dbd224"
api_key="49c747a1260e447bba1b4a53c6dbd224"
#send request to url
request=requests.get(url)
# Data obtained in dictionary form
#content=request.text
#Data obtained in json format
content=request.json();
#access title
for article in content["articles"]:
    print(article["title"])
