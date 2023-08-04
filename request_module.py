import requests
from bs4 import BeautifulSoup
r=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=54f4dc06be2a457cb226ce3c79c9afc9")
# print(r.text)
soup=BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
# import requests
# from bs4 import BeautifulSoup
# r=requests.get("https://adarshportfolio.blogspot.com/")
# # print(r.text)
# soup=BeautifulSoup(r.text,"html.parser")
# print(soup.prettify())