import scrapy
from training_python_scrapy.common.save_file import *
from scrapy.http.response.html import HtmlResponse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class RedditScrapy(scrapy.Spider):
    name: str = 'youtube_selenium'
    fileNo: int = 0

    def start_requests(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

        driver.get('https://www.lazada.com.ph/shop-laptops/')
        link_elements = driver.find_elements_by_xpath(
            '//*[@data-qa-locator="product-item"]//a[text()]')
        # link_elements = driver.find_elements_by_xpath(
        # '//a/@href')

        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)
        driver.quit()

    def parse(self, response: HtmlResponse, **kwargs):
        save_links_to_file(self, response.xpath("//img/@src"))
