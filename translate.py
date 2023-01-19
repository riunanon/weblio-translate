import requests
from bs4 import BeautifulSoup

url='https://ejje.weblio.jp/content/'

def search_weblio(word):
    response = requests.get(url+word)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def parse_item(word):
    soup = search_weblio(word)
    japanese = soup.find(class_='content-explanation ej').get_text().strip()
    return japanese

if __name__ == '__main__':
    english=input('単語を入力してください:')
    response=parse_item(english)
    print(response)
