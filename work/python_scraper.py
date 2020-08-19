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

def fetch(url: str) -> str:
    """
    urlのWebページを取得する.
    WebページのエンコーディングはContent-Typeヘッダーから取得する
    引数: url
    return: str型のHTML
    """
    
    r = requests.get(url)
    return r.text

def scrape(html: str, base_url: str) -> List[dict]:
    """
    HTMLから正規表現で書籍の情報を抜き出す.
    """

    books = []
    html = lxml.html.fromstring(html)
    html.make_links_absolute(base_url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')

        p = a.cssselect('p[itemprop="name"]')[0]
        title = p.text_content()

        books.append({'url': url, 'title': title})

    return books

def save(file_path: str, books: List[dict]):
    """
    csvに保存する
    """

    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, ['url', 'title'])
        writer.writeheader()
        writer.writerows(books)
    
# pythonコマンドで実行された場合にmainを呼ぶ
# モジュールとして他のファイルから呼び出されたときにmainが実行されないようにするための
# Pythonの一般的なイディオム

if __name__ == '__main__':
    main()

