import scrapy
from clubs_scraper.items import ClubsItem

NAME = "name"
LOCATION = "location"
STADIUM = "stadium"
MANAGER = "manager"

TEAM_COLUMN_ID = 1
LOCATION_COLUMN_ID = 2
STADIUM_COLUMN_ID = 6
MANAGER_COLUMN_ID = 9


class ClubSpider(scrapy.Spider):
    name = "club"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/La_Liga#Clubs"]

    def parse(self, response):
        club_table = response.xpath("//table[.//th[contains(text(), 'Manager')]]")
        club_rows = club_table.xpath(".//tr[position()>1]")
        for club in club_rows:
            item = ClubsItem()
            item[NAME] = club.xpath(f".//td[{TEAM_COLUMN_ID}]//text()").get()
            item[LOCATION] = club.xpath(f".//td[{LOCATION_COLUMN_ID}]//text()").get()
            item[STADIUM] = club.xpath(f".//td[{STADIUM_COLUMN_ID}]//text()").get()
            item[MANAGER] = club.xpath(f".//td[{MANAGER_COLUMN_ID}]//text()").get()
            yield item
