import scrapy
from training_python_scrapy.common.save_file import *
from scrapy.http.response.html import HtmlResponse


class RedditScrapy(scrapy.Spider):
    name: str = 'github'
    start_urls: str = ['https://github.com/MrParkerZ7']
    fileNo: int = 0

    def parse(self, response: HtmlResponse, **kwargs):
        save_links_to_file(self, response.xpath("//a/@href"))
