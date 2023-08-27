import scrapy


class DetikfinancescraperSpider(scrapy.Spider):
    name = "detikFinanceScraper"
    # allowed_domains = ["finance.detik.com"]
    start_urls = ["https://finance.detik.com/infrastruktur/d-6898532/sebulan-pertama-tarif-lrt-dapat-promo-jauh-dekat-rp-5000"]

    def parse(self, response):
        pass
