import requests
from bs4 import BeautifulSoup

def scrap_quotes(soup):
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    quotes_list = []


    for i in range(0, len(quotes)):
        quotes_dict_temp = {}

        quotes_dict_temp = {"tags": [], "author": authors[i].text, "quote": quotes[i].text}
        tagsforquote = tags[i].find_all('a', class_='tag')
        for tagforquote in tagsforquote:
            quotes_dict_temp["tags"].append(tagforquote.text)
        quotes_list.append(quotes_dict_temp)

    return(quotes_list)