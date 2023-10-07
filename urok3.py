import requests
from bs4 import BeautifulSoup

responce = requests.get("https://bank.gov.ua/ua/markets/currency-market")

if responce.status_code == 200:
    soup = BeautifulSoup(responce.text, features="html.parser")
    soup_list = soup.findAll('a', {"href":})
    result = soup_list[0].find("value")
    print(result.text)
# print(soup_list)    # print(soup) print(responce.content)