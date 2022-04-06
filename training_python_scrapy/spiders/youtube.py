from cgitb import html
from distutils import extension
from turtle import ht
from typing import Iterable, List
import scrapy


class RedditScrapy(scrapy.Spider):
    name: str = 'youtube'
    start_urls: str = ['https://www.youtube.com/']

    def parse(self, response):
        links = response.xpath("//link/@href")
        lines: List[str] = []

        for link in links:
            url: str = link.get()
            lines.append(url)

        with open(f"output/{self.name}.txt", 'w') as file:
            file.write('\n'.join(lines))
        print('XXX', lines)
