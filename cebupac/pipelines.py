import re
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class FilterFlightsPipeline(object):
    """This drops flight-tables which doesn't have the origin specified by the spider"""

    def process_item(self, item, spider):

        table = item['table']

        raw_origin = table.css('thead th:nth-child(1) strong::text').extract_first()

        # remove the unnecessary chars
        origin = re.sub(r'\ v\.v\.', '', raw_origin)

        if origin.upper() not in [origin.upper() for origin in spider.allowed_origins]:
            raise DropItem("{} isn't on the list of allowed ORIGINS.".format(origin))

        data = {
            'origin': origin,
            'destinations': table.css('tbody tr')
        }

        return data

class ExtractDestinationsPipeline(object):

    def process_item(self, item, spider):
        
        destinations = {}

        for dest in item['destinations'].css('tr'):
            place = dest.css('tr td:nth-child(1)::text').extract_first().strip()
            seats_left = dest.css('tr td:nth-child(2)::text').extract_first().strip()

            destinations[place] = {
                'seats_left': seats_left       
            }

        item['destinations'] = destinations

        return item
