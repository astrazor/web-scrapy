class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://example.com']

    def parse(self, response):

        for h4_element in response.css('h4'):

            title_text = h4_element.css('::text').get()

            self.log(f'Title: {title_text}')


if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
