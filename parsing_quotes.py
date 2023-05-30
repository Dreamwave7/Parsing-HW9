from bs4 import BeautifulSoup
import requests
import json
from pprint import *


def pagination():
    pages = []
    for i in range(24):
        url = f"http://quotes.toscrape.com/page/{i}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        verify = soup.find("div",class_= "quote")
        if verify:
            pages.append(url)
    return pages

urls = pagination()

quotes_list = []

def parse_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        # quotes = x.find_all("span",class_="text")
        for quote in quotes:
            text = quote.find("span",class_="text").text
            author = quote.find("small",class_="author").text
            tags_html = quote.find("div",class_="tags")
            tags = []
            for tag in tags_html.find_all("a",class_="tag"):
                tags.append(tag.text)

            seed = {
                "quote" : text,
                "author" : author,
                "tags" : tags
                }
            quotes_list.append(seed)
    return "Done"

def dump_to_json(list_quotess:list):
    with open("quotes.json","w") as file:
        json.dump(list_quotess, file)
        return "Done"

if __name__ == "__main__":
    for url in urls:
        parse_quotes(url)
    
    dump_to_json(quotes_list)
 
            
# '''
# Виберіть бібліотеку BeautifulSoup або фреймворк Scrapy.
# Ви повинні виконати скрапінг сайту http://quotes.toscrape.com.
# Ваша мета отримати два файли: qoutes.json, куди помістіть всю інформацію про цитати,
# з усіх сторінок сайту та authors.json, де буде знаходитись інформація про авторів зазначених цитат.
# Структура файлів json повинна повністю збігатися з попереднього домашнього завдання.
# Виконайте раніше написані скрипти для завантаження json файлів у хмарну базу даних для отриманих файлів.
# Попередня домашня робота повинна коректно працювати з новою отриманою базою даних.
# '''