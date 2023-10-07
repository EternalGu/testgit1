import sqlite3
import requests
from bs4 import BeautifulSoup

con = sqlite3.connect("examm_db.sl3")

responce = requests.get("https://coinmarketcap.com/")

if responce.status_code == 200:
    soup = BeautifulSoup(responce.text, features="html.parser")
    soup_list = soup.findAll('a', {"href": "/currencies/bitcoin/#markets"})
    result = soup_list[0].find("span")
    soup_list = soup.findAll('a', {"href": "/currencies/ethereum/#markets"})
    result2 = soup_list[0].find("span")
    soup_list = soup.findAll('a', {"href": "/currencies/bnb/#markets"})
    result3 = soup_list[0].find("span")
    name = result.text
    print(result.text)
    print(result2.text)
    print(result3.text)

cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS coins (name TEXT) ")
#cur.execute("INSERT INTO coins (name) values ('name')")
cur.execute("SELECT rowid, name FROM coins")

con.commit()
print(cur.fetchall())
con.close()