import requests
import send_email

#url of newsapi.org
url="https://newsapi.org/v2/everything?q=tesla&from=2023-04-10&sortBy=publishedAt&apiKey=49c747a1260e447bba1b4a53c6dbd224"
api_key="49c747a1260e447bba1b4a53c6dbd224"
#send request to url
request=requests.get(url)
# Data obtained in dictionary form
#content=request.text
#Data obtained in json format
content=request.json();
msg=""
#access title
for article in content["articles"]:
    if article["title"] is not None:
        #print(article["title"])
        msg=msg + article["title"] + "\n" \
        + article["description"] + "\n" \
        + "\n" + article["url"] + 2 * "\n"

#Convert entire message to utf-8 to get rid of UnicodeEncodeError
msg=msg.encode(encoding='utf-8' )
send_email.send_email(msg)