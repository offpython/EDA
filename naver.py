import requests
import pandas as pd
# from urllib.request.Request
from bs4 import BeautifulSoup

url =  "https://finance.naver.com/marketindex/"
response = requests.get(url)
# requests.get(), requests.post()
# response.text
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

exchangeList = soup.select("#exchangeList > li")

# 4개의 데이터 수집 (uptown은 오류로 제외)
exchange_datas = [] 
baseUrl = "https://finance.naver.com"

for item in exchangeList:
    data = {
        "title": item.select_one(".h_lst").text,
        "exchnage": item.select_one(".value").text,
        "change": item.select_one(".change").text,
        # "uptown" : item.select_one(".head_info.point_dn > .blind").text,
        "link": baseUrl + item.select_one("a").get("href")
    }
    exchange_datas.append(data)
df = pd.DataFrame(exchange_datas)
df.to_excel("./naverfinance.xlsx", encoding="utf-8")