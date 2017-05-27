import json
import xmltodict
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

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        response_json = self._convert_to_json(response.body)

        # We need to retrieve the HTML contents within the server response
        html_selector = Selector(text=response_json)

        for table in html_selector.css('table'):
            yield {
                'table' : table
            }

    def _convert_to_json(self, raw_data):
        """The server response sometimes switches from JSON to XML, this abstracts the main code from that.
        
        This function keeps the logic simple by checking the first character of the response:
            * '{' means JSON
            * '<' means XML
        """
        
        data = raw_data.decode('utf-8')

        if data[0] == '{':
            self.log("CebuPacific website responsded with a JSON data!")
            return json.loads(data)['d']['GetHtml']['Data']
        if data[0] == '<':
            self.log("CebuPacific website responsded with an XML data!")
            return xmltodict.parse(data)['d:GetHtml']['d:Data']


    def _get_origins(self, origins):
        """Splits the comma-separated ORIGIN values, returns None if passed with None."""

        if origins is None:
            return None
        
        return origins.split(',')
