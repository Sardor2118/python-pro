import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def main():
    url = 'https://quotes.toscrape.com/'
    async with aiohttp.ClientSession() as session:
        while True:
            page_counter = 0
            url += f'page/{page_counter+1}/'
            async with session.get(url) as response:
                try:
                    web_content = await response.text()
                    content = BeautifulSoup(web_content, 'html.parser')
                    all_quotes = content.find_all(class_='quote')
                    all_info = []
                    for quote in all_quotes:
                        text = quote.find(class_='text')
                        author = quote.find(class_='author')
                        tags = quote.find(class_='tags').find(class_='keywords').attrs.get('content')
                        all_info.append([text.text, author.text, tags])
                except:
                    print('all_info')
                    break
asyncio.run(main())

