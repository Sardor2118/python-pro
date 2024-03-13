import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parse_book_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    books_data = []
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        image_url = f"http://books.toscrape.com/{book.img['src'].replace('../', '')}"
        books_data.append({
            'Название книги': title,
            'Цена': price,
            'Наличие на складе': availability,
            'Ссылка на фото': image_url
        })
    return books_data

async def main():
    url = 'http://books.toscrape.com/'
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        books_data = await parse_book_data(html)
        print(books_data)

asyncio.run(main())
