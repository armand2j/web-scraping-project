import scrapy


class ClubsItem(scrapy.Item):
    name = scrapy.Field()
    location = scrapy.Field()
    stadium = scrapy.Field()
    manager = scrapy.Field()
