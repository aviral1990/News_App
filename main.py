import requests
import send_email

#Topic for fetching news
topic = "fitness"

#url of newsapi.org
url="https://newsapi.org/v2/everything?q=" + topic + "&from=2023-04-10&sortBy=publishedAt&apiKey=49c747a1260e447bba1b4a53c6dbd224&language=en"
api_key="49c747a1260e447bba1b4a53c6dbd224"
#send request to url
request=requests.get(url)
# Data obtained in dictionary form
#content=request.text
#Data obtained in json format
content=request.json();
msg=""
#access title
for article in content["articles"][:20]:  #only 20 articles
    if article["title"] is not None:
        #print(article["title"])
        msg= "Subject: Today's News" + "\n" + msg + article["title"] + "\n" \
        + article["description"] + "\n" \
        + "\n" + article["url"] + 2 * "\n"

#Convert entire message to utf-8 to get rid of UnicodeEncodeError
msg=msg.encode(encoding='utf-8' )
send_email.send_email(msg)