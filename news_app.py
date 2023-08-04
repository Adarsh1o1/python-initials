import requests,json
types=input("what type of news you want?(category) ")
url = (f"https://newsapi.org/v2/everything?q={types}&from=2023-02-25&sortBy=publishedAt&apiKey=54f4dc06be2a457cb226ce3c79c9afc9")
response = requests.get(url)
news= json.loads(response.text)
# print(news,type(news))
for article in news["articles"]:
    print("url- ",article["url"])
    print("Image url- ",article["urlToImage"])
    print("Date- ",article["publishedAt"])
    print("Title- ",article["title"])
    print("Description- ",article["description"])
    print("Content- ",article["content"])
    print("<>-------------------------------------------------------------------------------------------<>")

# (f"https://newsapi.org/v2/everything?q={types}&from=2023-02-25&sortBy=publishedAt&apiKey=54f4dc06be2a457cb226ce3c79c9afc9")