import scrapy
from scrapy.crawler import CrawlerProcess


class BcbSpider(scrapy.Spider):
    name = 'Bcb'
    allowed_domains = ['bcb.gov']
    start_urls = ['https://www4.bcb.gov.br/pec/poupanca/poupanca.asp']

    def parse(self, response):
        sel = scrapy.Selector(response)
        scrapy_base = sel.xpath('//td[@class="fundoPadraoAClaro1a"]//text()').extract()
        lista_rend = open('rendimento.txt', 'w')
        for i in range(0, len(scrapy_base), 8):
            lista_rend.write(scrapy_base[i][:-2] + '\n')
            lista_rend.write(scrapy_base[i+4][:-2] + '\n')
        lista_rend.close()
        pass


rem1 = CrawlerProcess()
rem1.crawl(BcbSpider)
rem1.start()
