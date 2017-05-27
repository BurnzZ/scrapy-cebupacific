import json
import scrapy
from scrapy.selector import Selector

class SeatSaleSpider(scrapy.Spider):
    """This spider crawls the CebuPacific website seat sale page."""

    name = "seat-sale"

    allowed_domains = ["cebupacificair.com"]
    start_urls = ['https://www.cebupacificair.com/_api/ceb/gethtml?name=%27NumberOfSeats%27']

    def __init__(self, origins=None):
        """
        :param origins: comma-separated ORIGIN of flights to look for
        """

        self.allowed_origins = self._get_origins(origins) or []

        self.allowed_origins = ['Manila']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        response_json = json.loads(response.body)

        # We need to retrieve the HTML contents within the server response
        html_selector = Selector(text=response_json['d']['GetHtml']['Data'])

        for table in html_selector.css('table'):
            yield {
                'table' : table
            }

    def _get_origins(self, origins):
        """Splits the comma-separated ORIGIN values, returns None if passed with None."""

        if origins is None:
            return None
        
        return origins.split(',')
