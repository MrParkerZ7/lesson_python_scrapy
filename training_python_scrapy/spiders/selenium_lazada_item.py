import scrapy
from training_python_scrapy.items import LazadaItem
from training_python_scrapy.common.save_file import *
from scrapy.http.response.html import HtmlResponse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.loader import ItemLoader


class RedditScrapy(scrapy.Spider):
    name: str = 'youtube_selenium_item'
    fileNo: int = 0

    def start_requests(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

        driver.get('https://www.lazada.com.ph/shop-laptops/')
        link_elements = driver.find_elements_by_xpath(
            '//*[@data-qa-locator="product-item"]//a[text()]')

        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)
        driver.quit()

    def parse(self, response: HtmlResponse, **kwargs):
        item = ItemLoader(item=LazadaItem(), selector=response)
        
        item.add_xpath(
            'name', '//h1/text()')
        item.add_xpath(
            'price', '//span[@class="pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]/text()')
        item.add_xpath(
            'image', '//img[@class="pdp-mod-common-image gallery-preview-panel__image"]/@src')

        yield item.load_item()
