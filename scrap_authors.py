import requests
from bs4 import BeautifulSoup

def scrap_authors(soup, main_link):
    abouts = soup.find_all("a", string = "(about)")
    authors = []
    author_fullnames = []
    for about in abouts:
        author = {}
        author_link = main_link + about["href"]
        author_soup = BeautifulSoup(requests.get(author_link).text, "lxml")
        fullname = author_soup.find("h3", class_="author-title")
        if fullname in author_fullnames:
            continue
        author_fullnames.append(fullname)
        author["fullname"] = author_soup.find("h3", class_="author-title").text
        author["born_date"] = author_soup.find("span", class_= "author-born-date").text
        author["born_location"] = author_soup.find("span", class_ = "author-born-location").text
        author["description"] = author_soup.find("div", class_= "author-description").text
        authors.append(author)
    return authors


