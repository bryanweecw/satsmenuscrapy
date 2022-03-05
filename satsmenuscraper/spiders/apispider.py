import json
import scrapy

start_url = 'https://satscampuseats.yale-nus.edu.sg/api/v1/staticmenus'


class newspider(scrapy.Spider):
    name = "scrapesatsapi"

    def start_requests(self):
        headers = {
            "Host": "satscampuseats.yale-nus.edu.sg",
            "dt": #date&timegetfromchrome,
            "sgt": #keygoesheregetfromchrome,
            "Authorization": #getfromchrome,
            "xid": #getfromchrome,
        }  # update as needed (check your network request headers in chrome)
        yield scrapy.Request(
            start_url, headers=headers, callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.body)
        yield data
