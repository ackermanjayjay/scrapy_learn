import scrapy 

class ChocolatespiderSpider(scrapy.Spider):

    #the name of the spider
    name = 'book'

    #the url of the first page that we will start scraping
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):

        #here we are looping through the products and extracting the name, price & url
        products = response.css('article')
        for product in products:
            #here we put the data returned into the format we want to output for our csv or json file
            yield{
                'title' : product.css('h3>a::text').get(),
                'price' : product.css("div>p::text").get(),
            }