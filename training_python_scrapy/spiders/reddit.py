from cgitb import html
from distutils import extension
import json
from turtle import ht
import scrapy


class RedditScrapy(scrapy.Spider):
    name: str = 'reddit'
    start_urls: str = ['https://www.reddit.com/r/cats', ]

    def parse(self, response):
        links = response.xpath("//img/@src")
        html = ""

        for link in links:
            url = link.get()
            if any(extension in url for extension in [".jpg", ".gif", ".png"]):
                html += """
                <a href="{url}" target="_blank">
                <img src="{url}" height="33%" width="33%"/> <a/>
                """.format(
                    url=url)

                with open(f"output/{self.name}.html", "w") as page:
                    page.write(html)
                    page.close()
