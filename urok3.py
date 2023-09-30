import requests
from bs4 import BeautifulSoup

responce = requests.get("https://coinmarketcap.com/")
# print(responce.content)
coins = ("bitcoin", "xrp")
if responce.status_code == 200:
    soup = BeautifulSoup(responce.text, features="html.parser")
    # print(soup)
    soup_list = soup.findAll('a', {"href": "/currencies/", coins: "/#markets"})
    # print(soup_list)
    result = soup_list[0].find("span")
    print(result.text)
