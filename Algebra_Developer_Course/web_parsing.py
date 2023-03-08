import requests
from bs4 import BeautifulSoup

class Book:
    def __init__(self, rating, title, price) -> None:
        self.rating = rating
        self.title = title
        self.price = price

    #CSV format
    def __str__(self) -> str:
        return f"{self.rating}, {self.title}, {self.price}"

#print(raw_data)

price_selector = ".price_color"
rating_selector = ".star-rating"
title_selector = ".product_pod h3 a"

rating_description = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

URL = "http://books.toscrape.com/"
response = requests.get(URL)
raw_data = response.content

website = BeautifulSoup(raw_data, "html.parser")

prices = website.select(price_selector)
print(prices)

prices_parsed = []
for price in prices:
    prices_parsed.append(price.string)
print(prices_parsed)


titles = website.select(title_selector)
print(titles)

titles_parsed = []
for title in titles:
    titles_parsed.append(title.string)
print(titles_parsed)


ratings = website.select(rating_selector)
print(ratings)

ratings_parsed = []
for rating in ratings:
    for name, star_number in rating_description.items():
        if name in rating["class"]:
            ratings_parsed.append(star_number)
print(ratings_parsed)



with open("books.csv", "w", encoding="utf-8") as file_stream:
    parsed_data = zip(prices_parsed, titles_parsed, ratings_parsed)
    for price, title, rating in parsed_data:
        book = Book(rating = rating, title = title, price = price)
        row = f"{book}\n"
        file_stream.write(row)
