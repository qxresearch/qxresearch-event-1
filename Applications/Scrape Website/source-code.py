from webxplore import WebScraper

# Initialize variable
link = input('Enter link to the website that you want to scrape: ')

# Getting text content from the website
scrapedContent = WebScraper.ScrapeWebsite(link)

print(scrapedContent.return_article())
