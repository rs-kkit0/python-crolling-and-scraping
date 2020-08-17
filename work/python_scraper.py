import csv
from typing import List
import requests
import lxml.html

def main():
    """
    main処理.
    fetch(), scrape(), save()を呼び出す.
    """

    url = 'https://gihyo.jp/dp'
    html = fetch(url)
    books = scrape(html, url)
    save('books.csv', books)

def fetch(url: string) -> str:
    """
    urlのWebページを取得する.
    WebページのエンコーディングはContent-Typeヘッダーから取得する
    引数: url
    return: str型のHTML
    """
    