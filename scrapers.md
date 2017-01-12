# Web Scrapers

When you can't get data from an API, you can get it directly from the website and build your own Dataset.

![](https://www.evernote.com/shard/s150/sh/cbe07b70-82f9-4b8f-ade1-52811cb37740/63ec04884b9dd804/res/bb10829c-30f3-4558-a00e-e75b46fde1f2/skitch.png?resizeSmall&width=832)

The openelections project relies on scrapers to find data from various local

[http://www.openelections.net/](http://www.openelections.net/)

## Simplest Scraper - Copy/Paste
[http://www.realclearpolitics.com/epolls/other/trump_favorableunfavorable-5493.html#polls](http://www.realclearpolitics.com/epolls/other/trump_favorableunfavorable-5493.html#polls)

## Finding Hidden APIs
* [http://data.desmoinesregister.com/iowa-caucus/candidate-tracker/index.php](http://data.desmoinesregister.com/iowa-caucus/candidate-tracker/index.php)

* [http://www.gallup.com/poll/113980/Gallup-Daily-Obama-Job-Approval.aspx](http://www.gallup.com/poll/113980/Gallup-Daily-Obama-Job-Approval.aspx)

* [http://polling.reuters.com/#poll/TR130](http://polling.reuters.com/#poll/TR130)

### Dc Courts Example
[https://www.dccourts.gov/cco/maincase.jsf](https://www.dccourts.gov/cco/maincase.jsf)

## Manipulating URLs
Hidden APIs are not documented, you can manipulate URLs to explore them, to paginate, etc.

## Try It


## CSS Selectors

Reference Sheet:

[http://www.w3schools.com/cssref/css_selectors.asp](http://www.w3schools.com/cssref/css_selectors.asp)

Lets try one together:

[http://www.presidency.ucsb.edu/debates.php](http://www.presidency.ucsb.edu/debates.php)

1. Scrape the Date, Title, and Text of each speech.

## Some Example Scrapers

These links are private, you won't be able to access them.

* [Census](https://github.com/fivethirtyeight/scrapers/blob/master/census/historical_age.py)
* [CeoTenure](https://github.com/fivethirtyeight/scrapers/blob/master/ceotenure/worldofceos.py)
* [Change.org Petitons](https://github.com/fivethirtyeight/scrapers/blob/master/change_org/scrape.py)
* [Tea Party Members](https://github.com/fivethirtyeight/scrapers/blob/master/congress/scrape_teaparty.py)
* [Candidate Speeches from CSPAN](https://github.com/fivethirtyeight/scrapers/blob/master/cspan/scrape.rb)
* [Candidate Speeches from Presidency Project](https://github.com/fivethirtyeight/scrapers/blob/master/presidency_project/scraper.rb)
* [World Flags](https://github.com/fivethirtyeight/scrapers/tree/master/flagscraper)
* [Killed By Police](https://github.com/fivethirtyeight/scrapers/blob/master/killedbypolice/killedbypolice.py)
* [Gallup Polls](https://github.com/fivethirtyeight/scrapers/blob/master/gallupscraper/scrape.py)

The FiveThirtyEight Poling Pipeline

* Tweet (https://twitter.com/ascheink/status/789176088278601728)
* `#GeneralModel` slack channel

## Try It

Find a scraper that is written in python on github. Lets take a look at what it is doing. Present your findings to the class.

## Try It
Think of a dataset you'd want to scrape. Tell me how you're going to get the data. Explain in detail whether you will use a hidden API or scrape the data. If you're going to scrape the data, include the CSS selectors you want to scrape. 

### Bonus 
1. Submit a python file with comments stream on how this will be done. 

2. Add functions and loops too. 

## Scraping Ethics / Caveats

[http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/7](http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/7)

## Additional Resources

* HTTP Examples & Reference - [http://httpbin.org/](http://httpbin.org/)
* Scraper tools - [https://gist.github.com/cassidoo/9b1791a47411dd1253af2e5e8ef7c72a](https://gist.github.com/cassidoo/9b1791a47411dd1253af2e5e8ef7c72a)

## Additional Readings
* https://scraperwiki.com/2011/06/why-the-government-scraped-itself/
* http://robertorocha.info/on-the-ethics-of-web-scraping/
* http://opencivicdata.readthedocs.io/en/latest/scrape/basics.html
* http://datajournalismhandbook.org/1.0/en/getting_data_3.html