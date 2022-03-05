# Requirements

1. Python 3.10
2. Scrapy
3. Selenium
4. ChromeDriver

# Set-up

1. Update `satsmenuscraper/spiders/menuspider.py` with your appropriate NUS login details (lines 31 & 34)
2. Update `satsmenuscraper/spiders/apispider.py` with the headers for querying the SATS menu api. You can find these by going to the SATS menu website, logging in, and monitoring the request object in the network tab of your browser when you click on the individual menu items to view nutritional information. The required header keys are already provided for you.

# How to run

1. Run `scrapy crawl menuscraper -o menu.json` (run daily at midnight to update menu for the day)
2. Run `scrapy crawl scrapesatsapi -o satsapi.json` (only need to run weekly, which is when SATS uploads the following week's menu; or run whenever errors noticed, or menu seems out of sync)
3. Run `cd ./tutorial`
4. Run `python3 textfilegen.py`
5. Stonks
