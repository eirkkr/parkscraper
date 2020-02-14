import pandas as pd

import scrapy
import parkscraper.get_athlete_urls as get_athlete_urls


class ParkSpider(scrapy.Spider):
    name = "parkspider"

    def start_requests(self):

        urls = get_athlete_urls.get_athlete_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        results = pd.DataFrame(
            columns=[
                "Event",
                "Run Date",
                "Gender Pos",
                "Overall Position",
                "Time",
                "Age Grade",
            ]
        )
        for row in response.xpath('//*[@id="results"]'):
            results["Event"] = results["Event"].append(
                row.xpath("td[0]//text()").extract_first()
            )
            results["Run Date"] = row.xpath("td[1]//text()").extract_first()
            results["Gender Pos"] = row.xpath("td[2]//text()").extract_first()
            results["Overall Position"] = row.xpath("td[3]//text()").extract_first()
            results["Time"] = row.xpath("td[4]//text()").extract_first()
            results["Age Grade"]: row.xpath("td[5]//text()").extract_first()
