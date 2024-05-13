import requests
from bs4 import BeautifulSoup
from scrap_quotes import scrap_quotes
from scrap_authors import scrap_authors
from dump_to_json import dump_to_json


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

dump_to_json(scrap_quotes(soup), "qoutes.json")
dump_to_json(scrap_authors(soup, url), "authors.json")
