from cgitb import html
from distutils import extension
from turtle import ht
from typing import Iterable, List
import scrapy


class RedditScrapy(scrapy.Spider):
    name: str = 'github'
    start_urls: str = ['https://github.com/MrParkerZ7']

    def parse(self, response):
        links = response.xpath("//a/@href")
        lines: List[str] = []

        for link in links:
            url: str = link.get()
            if(url.startswith('https://')):
                lines.append(url)
            elif(url != ''):
                lines.append(self.start_urls[0] + url)

        with open(f"output/{self.name}.txt", 'w') as file:
            file.write('\n'.join(lines))
