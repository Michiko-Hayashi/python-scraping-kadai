import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/articles/73c2dd02d382c283dfe1bb75eb754703f1c0fc9c"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# 本文ブロックを取得
body = soup.select_one("div.article_body")

if body:
    for p in body.find_all("p"):
        text = p.get_text(strip=True)
        if text:
            print(text)
else:
    print("記事本文が見つかりませんでした")
