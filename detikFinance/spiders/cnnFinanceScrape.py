import scrapy


class CnnfinancescrapeSpider(scrapy.Spider):
    name = "cnnFinanceScrape"
    # allowed_domains = ["www.cnnindonesia.com"]
    start_urls = ["https://www.cnnindonesia.com/ekonomi/20230801071400-85-980229/daftar-harga-bbm-terbaru-di-spbu-pertamina-cs-usai-naik-per-1-agustus"]

    def parse(self, response):
        article=response.css("div.detail-text")
        for article in article:
            yield{
                "article":article.css("p::text").getall()
            }
