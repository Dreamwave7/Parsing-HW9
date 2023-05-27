from models import *
from bs4 import BeautifulSoup
import requests
from pprint import pp
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

url = "http://books.toscrape.com/"
html = requests.get(url)

def parsing():
    store = []
    rate_to_number = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    if html.status_code == 200:
        soup = BeautifulSoup(html.content, "html.parser")
        books = soup.select("section")[0].find_all("article", class_="product_pod")
        for book in books:
            img = f"{url}{book.find('img')['src']}"
            rating = book.find("p",class_="star-rating")["class"][1]
            grade = rate_to_number.get(rating)
            title = book.find("h3").find("a")["title"]
            price =  book.find("p",class_="price_color").text.replace("£","")
            store.append({
                "img":img,
                "title":title,
                "rating":grade,
                "price":price,
                })
    return store

def release_db():
    store = parsing()
    engine = create_engine("sqlite:///books.db")
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for dct in store:
        book = Book(
            img_url =dct.get("img"),
            rating = dct.get("rating"),
            title = dct.get("title"),
            price = dct.get("price"),
            )
        session.add(book)
    session.commit()
release_db()