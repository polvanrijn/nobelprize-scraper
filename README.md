# Nobelprize webscraper
This scraper scrapes off information from the Nobelprize database using a Python tool called "Scrapy".

## Extracted information
For each Nobelprize and each year there are multiple nominees and multiple nominators. So every year there are multiple nominations. In one nomination there is always one person or there are multiple persons who are being nominated (usually authors) and who are nominating (usually professors from an university).

Per nomination the following information is beeing extracted:
* year of the nomination
* the identification number of the nomination
* the url the information was extraced from
* (optionally) possible comments

Extracted information per nomination per nominee (if there are multiple nominees, data is extracted separately):
* name of the nominee
* (optionally) gender of the nominee
* (optionally) date of birth
* (optionally) date of death
* (optionally) profession of nominee
* (optionally) city where nominee lives/lived
* (optionally) country/nationallity
* (optionally) motivation of the nominee for applying for the Nobelprize

Extracted information per nomination per nominator (if there are multiple nominators, data is extracted separately):
* name of the nominator
* (optionally) gender of the nominator
* (optionally) date of birth
* (optionally) date of death
* (optionally) profession of nominator
* (optionally) university of nominator
* (optionally) city where nominee lives/lived
* (optionally) country/nationallity

## How it works
This project contains two different scraping scripts:
* 'url_spider' for grabbing all links within a selected time scrope (in our case the literary Nobelprize between 1901 and 1966)
* 'nobelscraper' scraping the information described in section "Extracted information"

## How to use it
First make sure you have [Python](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installing/) and Scrapy (use 'pip install Scrapy') installed.
You might have to install [Visual C++ 2015 Build Tools](http://landinghub.visualstudio.com/visual-cpp-build-tools) if you are working on Windows.
Now open 'cmd' if you are working on Windows and navigate to your spider

'''
cd <path to your folder>\nobelprize\nobelprize\spiders
'''

First generate all urls you want to scrape:

'''
scrapy crawl url_spider > urls.txt
'''

If you want to download all urls, then uncomment:
'''
    # f = open("urls.txt",'r')
    # start_urls = [url.strip() for url in f.readlines()]
    # f.close()
'''

And comment:

'''
    start_urls = [
        'http://www.nobelprize.org/nomination/archive/show.php?id=5469',
        'http://www.nobelprize.org/nomination/archive/show.php?id=17599',
        'http://www.nobelprize.org/nomination/archive/show.php?id=1046'
    ]
'''

Then you can run the scraper by running following command:
'''
scrapy crawl nobelscraper -o <name of your output file>.csv
'''

Afterwards you can open the csv with Excel or Libreoffice.