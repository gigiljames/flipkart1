import scrapy
from ..items import Flipkart1Item

class Flipscrape1Spider(scrapy.Spider):
    name = 'flipscrape1'
    #allowed_domains = ['www.flipkart.com']
    # start_urls = ['http://www.flipkart.com/']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/81.0.4044.108 Safari/537.36',
        }
        url = r'https://www.flipkart.com/laptops-store?fm=neo%2Fmerchandising&iid=M_ff617f0e-2c96-4903-8ea4-0fec6b257827_1_372UD5BXDFYS_MC.WB1CFS0X26D1&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop~Laptops_WB1CFS0X26D1&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=WB1CFS0X26D1'
        yield scrapy.Request(url=url, callback=self.parse_page, headers=headers)

    def parse_page(self, response):
        items = Flipkart1Item()
        html_response = response.xpath('//div[@class="_2nRPpA"]')
        print(html_response)
        for row in html_response:
            print(row)
            name = row.xpath('div[@class="_1Ni40J"]/div[@class="_1kLt05"]/a/div[@class="_1W9f5C"]/div/text()').extract()
            Rating = row.xpath('div[@class="_1Ni40J"]/div[@class="_1kLt05"]/a/div[@class="_3VDxyD"]/div/text()').extract()
            Num_Rating = row.xpath('div[@class="_1Ni40J"]/div[@class="_1kLt05"]/a/div[@class="_3VDxyD"]/span[@class="_34hpFu"]/span/text()').extract()
            Num_Reviews = row.xpath('div[@class="_1Ni40J"]/div[@class="_1kLt05"]/a/div[@class="_3VDxyD"]/span[@class="_34hpFu"]/span/span/text()').extract()
            Price = row.xpath('div[@class="_1Ni40J"]/div[@class="_1kLt05"]/a/div[@class="_2wYYVP"]/div[@class="_25b18c"]/div[@class="_30jeq3 UMT9wN"]/text()').extract()
            Product_Specs = row.xpath('div[@class="_1Ni40J"]/div[@class="_1kLt05"]/ul[@class="_1Sq2Fs"]/li/text()').extract()a
            Discount = row.xpath('div[@class="_1Ni40J"]/div[@class="_1kLt05"]/a/div[@class="_2wYYVP"]/div[@class="_25b18c"]/div[@class="_3Ay6Sb _2FuKQX"]/span/text()').extract()
            items['Product_Name'] = ''.join(name)
            items['Rating'] = ''.join(Rating)
            items['Num_Rating'] = ''.join(Num_Rating)
            items['Num_Reviews'] = Num_Reviews[1]
            items['Price'] = ''.join(Price)
            items['Product_Specs'] = ', '.join(Product_Specs)
            if len(Discount)==0:
                items['Discount'] = 'N.A'
            else:
                items['Discount'] = ''.join(Discount)
            yield items

        



#  'Product_Name':'//div[@class="_1W9f5C"]/div/text()'
# 'Rating':'//div[@class="_3VDxyD"]/div/text()'
# 'Num_Rating':'//span[@class="_34hpFu"]/span/text()'
# 'Num_Reviews':'//span[@class="_34hpFu"]/span/span/text()'
# 'Price': '//div[@class="_30jeq3 UMT9wN"]/text()'
# 'Product_Specs':'//ul[@class="_1Sq2Fs"]/li/text()'
# 'Discount': '//div[@class="_25b18c"]/div[@class="_3Ay6Sb _2FuKQX"]/span/text()'
