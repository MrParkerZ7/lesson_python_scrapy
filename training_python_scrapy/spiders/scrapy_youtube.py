import scrapy
from training_python_scrapy.common.save_file import *
from scrapy.http.response.html import HtmlResponse


class RedditScrapy(scrapy.Spider):
    name: str = 'youtube'
    start_urls: str = ['https://www.youtube.com/']
    fileNo: int = 0

    def parse(self, response: HtmlResponse, **kwargs):
        save_links_to_file(self, response.xpath("//a/@href"))
        save_links_to_file(self, response.xpath("//link/@href"))
        save_links_to_file(self, response.xpath("//img/@src"))
