import requests
from bs4 import BeautifulSoup
import json
from pprint import *
from parsing_quotes import pagination


authors_links = [
    'http://quotes.toscrape.com/author/Albert-Einstein',
    'http://quotes.toscrape.com/author/J-K-Rowling',
    'http://quotes.toscrape.com/author/Jane-Austen',
    'http://quotes.toscrape.com/author/Marilyn-Monroe',
    'http://quotes.toscrape.com/author/Andre-Gide',
    'http://quotes.toscrape.com/author/Thomas-A-Edison',
    'http://quotes.toscrape.com/author/Eleanor-Roosevelt'
    ]

def parse_authors_link(url):
    response = requests.get(url)
    if response.status_code == 200:
        basic_url = "http://quotes.toscrape.com"
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("div", class_="quote")
        for link in links:
            full_link= basic_url+link.find_all("a")[0]["href"]
            if full_link not in authors_links:
                authors_links.append(full_link)
            else:
                continue
    return "done"

authors_info = []
def parse_authors_info(url:str):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        name = url.split("/")[-1]
        born_date = soup.find("div",class_="author-details").find("h3").find("span",class_="author-born-date").text
        where_born = soup.find("div",class_="author-details").find("h3").find("span",class_="author-born-location").text
        description = soup.find("div",class_="author-details").find("h3").find("div",class_="author-description").text.strip()
        
        author = {
            "name":name,
            "born":born_date+" "+where_born,
            "description": description
            }
        authors_info.append(author)

def dump_to_json(listt:list):
    with open("authors.json","w") as file:
        json.dump(listt,file)



if __name__ == "__main__":
    urls = pagination()
    for link in urls:
        parse_authors_link(link)

    for link in authors_links:
        parse_authors_info(link)
    
    dump_to_json(authors_info)









































# '''
# Виберіть бібліотеку BeautifulSoup або фреймворк Scrapy.
# Ви повинні виконати скрапінг сайту http://quotes.toscrape.com.
# Ваша мета отримати два файли: qoutes.json, куди помістіть всю інформацію про цитати,
# з усіх сторінок сайту та authors.json, де буде знаходитись інформація про авторів зазначених цитат.
# Структура файлів json повинна повністю збігатися з попереднього домашнього завдання.
# Виконайте раніше написані скрипти для завантаження json файлів у хмарну базу даних для отриманих файлів.
# Попередня домашня робота повинна коректно працювати з новою отриманою базою даних.
# '''






