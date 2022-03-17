# Requirements

1. Python 3.10
2. Scrapy
3. Selenium
4. ChromeDriver

# How to run

1. Run `scrapy crawl menuscraper -o menu.json` (run daily at midnight to update menu for the day)
2. Run `scrapy crawl scrapesatsapi -o satsapi.json` (only need to run weekly, which is when SATS uploads the following week's menu; or run whenever errors noticed, or menu seems out of sync)
3. Run `python3 textfilegen.py`
4. Stonks (menu written in summary.text)

## Set-up

1. Run the following in your terminal (remove square brackets, keep double quotes (where applicable), replace placeholder values):

```
export USER=[your_username]
export PASS=[your_username]
export DT="[datetime_from_chrome _request_header]"
export SGT="[sgt_from_chrome _request_header]"
export AUTHORIZATION="[authorization_from_chrome _request_header]"
export XID="[xid_from_chrome _request_header]"
```

## Copy-pastable Scripts

```
scrapy crawl menuscraper -o menu.json
scrapy crawl scrapesatsapi -o satsapi.json
python3 textfilegen.py
```
