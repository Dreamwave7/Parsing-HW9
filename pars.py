import requests
from bs4 import BeautifulSoup
from pprint import *

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


p = soup.select(".text")
pprint(p[1])