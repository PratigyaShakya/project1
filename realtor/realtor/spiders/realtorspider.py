import scrapy

class Realtorspider(scrapy.Spider):
    name="realtor"
    allowed_domains=["realtor.com"]
    start_urls=[
        "http://www.realtor.com/realestateandhomes-detail/2002-5th-Ave-Apt-5B_New-York_NY_10035_M35780-75634"]

def parse(self,response):
    for sel in response.xpath('//ul/li'):
        title = sel.xpath('a/text()').extract()
        streetadd = sel.xpath('a/text()').extract()
        area = sel.xpath('text()').extract()
        overview = sel.xpath('text()').extract()
    print title, link, desc

