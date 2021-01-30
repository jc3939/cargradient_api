import re
import json
import datetime as dt
import logging

from scrapy import Spider, Request
from myKbbBot.items import MykbbbotItem
from scrapy.shell import inspect_response as debug


logger = logging.getLogger()

class CarSpecsSpider(Spider):

    name = "myKbbBot"
    #start_urls: an attribute listing the URLs the spider will start from
    allowed_domains = ['www.kbb.com']

    #allowed_urls: the main domain of the website you want to scrape
    start_urls = ['https://www.kbb.com/compare-cars/results/?vehicleids=']

    total_vehicleIds = 0

    valid_vehicleIds = 0

    def parse(self, response):
        result_pages = ['https://www.kbb.com/compare-cars/results/?vehicleids={}'.format(str(x)) for x in range(582911,106217,-1)]
        for url in result_pages:
            yield Request(url=url, callback=self.parse_result_page)


    def parse_result_page(self, response):

        self.total_vehicleIds += 1

        vehicleId = response.request.url.split('=')[1]

        debug(response, self)

        page_source = response.xpath('//*[contains(text(),"window.__ERROR_PAGE__ = false;window.__APOLLO_STATE__")]').extract()[0]


        specs_data = json.loads(re.findall('\{.*\}',page_source)[0])

        item = MykbbbotItem()

        if '$ROOT_QUERY.compareResults({"vehicleIds":["'+vehicleId+'"]}).vehicles.0' in specs_data:
            self.valid_vehicleIds += 1
            item['query_date'] = dt.date.today()
            item['query_url'] = response.request.url
            item['vehicleId'] = vehicleId
            item['car_year'] = specs_data['$ROOT_QUERY.compareResults({"vehicleIds":["'+vehicleId+'"]}).vehicles.0']['year']
            item['car_make'] = specs_data['$ROOT_QUERY.compareResults({"vehicleIds":["'+vehicleId+'"]}).vehicles.0']['manufacturer']
            item['car_model'] = specs_data['$ROOT_QUERY.compareResults({"vehicleIds":["'+vehicleId+'"]}).vehicles.0']['model']
            item['car_trim'] = specs_data['$ROOT_QUERY.compareResults({"vehicleIds":["'+vehicleId+'"]}).vehicles.0']['trimName']
            item['basic_info'] = specs_data['$ROOT_QUERY.compareResults({"vehicleIds":["'+vehicleId+'"]}).vehicles.0']
            item['specs_info'] = specs_data['$ROOT_QUERY.compareResults({"vehicleIds":["'+vehicleId+'"]}).vehicles.0.specs']
            logging.info("Now queried %s vehicleIds, %s of them are valid." % (self.total_vehicleIds, self.valid_vehicleIds))
            yield item
        else:
            logging.info("Now queried %s vehicleIds, %s of them are valid." % (self.total_vehicleIds, self.valid_vehicleIds))