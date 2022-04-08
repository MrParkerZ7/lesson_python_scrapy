from typing import List
import scrapy
from scrapy.utils.project import get_project_settings
from training_python_scrapy.common.save_file import *
from scrapy.http.response.html import HtmlResponse
from selenium import webdriver
from chromedriver_py import binary_path
from webdriver_manager.chrome import ChromeDriverManager


class RedditScrapy(scrapy.Spider):
    name: str = 'se_youtube'
    # start_urls: str = ['https://www.youtube.com/']
    # fileNo: int = 0

    def start_requests(self):
        settings = get_project_settings()
        # driver_path = settings['CHROME_DRIVER_PATH']
        # driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        # driver_path = 'D:\env_storeage\chrome_driver\chromedriver'
        driver_path = binary_path
        options = webdriver.ChromeOptions()
        options.headless = True
        # driver = webdriver.Chrome(driver_path, options=options)
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        # driver = webdriver.Chrome( options=options)

        driver.get('https://www.youtube.com/')
        link_elements = driver.find_elements_by_xpath(
            '//*[@data-qa-locator="product-item"]//a[text()]')

        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)

        driver.quit()

    def parse(self, response: HtmlResponse, **kwargs):
        print('XXX', response)
        save_links_to_file(self, response.xpath("//a/@href"))
        save_links_to_file(self, response.xpath("//link/@href"))
        save_links_to_file(self, response.xpath("//img/@src"))
        pass
