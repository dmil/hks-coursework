# Creatively Acquiring Data

Now that you understand some concepts behind the front-end stack like CSS selectors, we can use these tools to our advantage as we browse the web, and gather data when we find it in unexpected places.

## HTTP (Quick Review)
Before we start deconstructing websites, a quick review of HTTP requests.
http://httpbin.org/

Lets make some simple HTTP requests using the "postman" chrome extension.

## Taking a closer look at HTML in the browser

HTML is a tree
parts of tags

How div tags work, as well as classes and names.

### Modifying returned HTML

- Facebook photo change

## Using CSS selectors to find elements
(and Xpath) with "SelectorGadget"
http://www.presidency.ucsb.edu/

Reference Sheet:

[http://www.w3schools.com/cssref/css_selectors.asp](http://www.w3schools.com/cssref/css_selectors.asp)

Lets try one together:

[http://www.presidency.ucsb.edu/debates.php](http://www.presidency.ucsb.edu/debates.php)

1. Find the Date, Title, and Text of each speech with a CSS selector.

## And then using JavaScript to manipulate them

http://www.realclearpolitics.com/epolls/other/president_obama_job_approval-1044.html

<!-- $$("#polling-data-full tr:not(.rcpAvg2):not(.header):not(.final):not(.isInRcpAvg) td") -->


## What else can you tell about the website?

https://www.whitehouse.gov/interactive-budget
- Google Analytics
- Find Data (and clean it)

## Using CSS Selectors and Import.io to get data

http://import.io

<!-- $$("#polling-data-full tr:not(.rcpAvg2):not(.header):not(.final):not(.isInRcpAvg) td") -->

## Aside...a quick look at cookies
with "EditThisCookie"
http://lifehacker.com/5461114/fact-and-fiction-the-truth-about-browser-cookies

Cookies on Facebook - look them up in a cookie database.

How about FiveThirtyEight?

##  Additional notes about scrapers

When you can't get data from an API, you can get it directly from the website and build your own Dataset. I write most of my web scrapers in python or ruby. Unfortunately we won't have time to get into how to do that, but we will do some simple JavaScript based scraping in the console!

## Scrapers ... not beyond your reach!
Scrapers are used extensively by data journalists like myself...
![](https://www.evernote.com/shard/s150/sh/cbe07b70-82f9-4b8f-ade1-52811cb37740/63ec04884b9dd804/res/bb10829c-30f3-4558-a00e-e75b46fde1f2/skitch.png?resizeSmall&width=832)

There are some great civic technology projects that involve scraped data as well!

[http://www.openelections.net/](http://www.openelections.net/)

## Simplest Scraper - Copy/Paste
[http://www.realclearpolitics.com/epolls/other/trump_favorableunfavorable-5493.html#polls](http://www.realclearpolitics.com/epolls/other/trump_favorableunfavorable-5493.html#polls)

## Finding Hidden APIs
* [http://data.desmoinesregister.com/iowa-caucus/candidate-tracker/index.php](http://data.desmoinesregister.com/iowa-caucus/candidate-tracker/index.php) (do together)

* [http://www.gallup.com/poll/113980/Gallup-Daily-Obama-Job-Approval.aspx](http://www.gallup.com/poll/113980/Gallup-Daily-Obama-Job-Approval.aspx) (do together)

* [http://polling.reuters.com/#poll/TR130](http://polling.reuters.com/#poll/TR130) (do in pairs)

## Using JavaScript to get data


A function to find all colors on a webpage
```
// allcolors.js
// https://github.com/bgrins/devtools-snippets
// Print out CSS colors used in elements on the page.

(function () {
  // Should include colors from elements that have a border color but have a zero width?
  var includeBorderColorsWithZeroWidth = false;

  var allColors = {};
  var props = ["background-color", "color", "border-top-color", "border-right-color", "border-bottom-color", "border-left-color"];
  var skipColors = {
    "rgb(0, 0, 0)": 1,
    "rgba(0, 0, 0, 0)": 1,
    "rgb(255, 255, 255)": 1
  };

  [].forEach.call(document.querySelectorAll("*"), function (node) {
    var nodeColors = {};
    props.forEach(function (prop) {
      var color = window.getComputedStyle(node, null).getPropertyValue(prop),
        thisIsABorderProperty = (prop.indexOf("border") != -1),
        notBorderZero = thisIsABorderProperty ? window.getComputedStyle(node, null).getPropertyValue(prop.replace("color", "width")) !== "0px" : true,
        colorConditionsMet;

      if (includeBorderColorsWithZeroWidth) {
        colorConditionsMet = color && !skipColors[color];
      } else {
        colorConditionsMet = color && !skipColors[color] && notBorderZero;
      }

      if (colorConditionsMet) {
        if (!allColors[color]) {
          allColors[color] = {
            count: 0,
            nodes: []
          };
        }

        if (!nodeColors[color]) {
          allColors[color].count++;
          allColors[color].nodes.push(node);
        }

        nodeColors[color] = true;
      }
    });
  });

  function rgbTextToRgbArray(rgbText) {
    return rgbText.replace(/\s/g, "").match(/\d+,\d+,\d+/)[0].split(",").map(function(num) {
      return parseInt(num, 10);
    });
  }

  function componentToHex(c) {
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
  }

  function rgbToHex(rgbArray) {
    var r = rgbArray[0],
      g = rgbArray[1],
      b = rgbArray[2];
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
  }

  var allColorsSorted = [];
  for (var i in allColors) {
    var rgbArray = rgbTextToRgbArray(i);
    var hexValue = rgbToHex(rgbArray);

    allColorsSorted.push({
      key: i,
      value: allColors[i],
      hexValue: hexValue
    });
  }

  allColorsSorted = allColorsSorted.sort(function (a, b) {
    return b.value.count - a.value.count;
  });

  var nameStyle = "font-weight:normal;";
  var countStyle = "font-weight:bold;";
  function colorStyle(color) {
    return "background:" + color + ";color:" + color + ";border:1px solid #333;";
  };

  console.group("Total colors used in elements on the page: " + window.location.href + " are " + allColorsSorted.length);
  allColorsSorted.forEach(function (c) {
    console.groupCollapsed("%c    %c " + c.key + " " + c.hexValue + " %c(" + c.value.count + " times)",
      colorStyle(c.key), nameStyle, countStyle);
    c.value.nodes.forEach(function (node) {
      console.log(node);
    });
    console.groupEnd();
  });
  console.groupEnd("All colors used in elements on the page");

})();
```

A function to save JavaScript objects from the console.
```
(function(console){

    console.save = function(data, filename){

        if(!data) {
            console.error('Console.save: No data')
            return;
        }

        if(!filename) filename = 'console.json'

        if(typeof data === "object"){
            data = JSON.stringify(data, undefined, 4)
        }

        var blob = new Blob([data], {type: 'text/json'}),
            e    = document.createEvent('MouseEvents'),
            a    = document.createElement('a')

        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
        e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        a.dispatchEvent(e)
    }
})(console)
```

Venmo Example
https://venmo.com/api/v5/users/405075/feed?until=1481599799&limit=20

(can build network graph...)

### Manipulating URLs
Hidden APIs are not documented, but if they are built in a RESTful way, you can manipulate URLs to explore them and get to the data you need.

### Poorly Built Websites are hard to Scrape
...but there is almost always a way

Dc Courts Example
[https://www.dccourts.gov/cco/maincase.jsf](https://www.dccourts.gov/cco/maincase.jsf)


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

## Scraping Ethics / Caveats

[http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/7](http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/7)

## Additional Resources

* Import.io - really useful to scrape things, with this and some knowledge of CSS selectors you can be pretty resourceful.

* Scraper tools - [https://gist.github.com/cassidoo/9b1791a47411dd1253af2e5e8ef7c72a](https://gist.github.com/cassidoo/9b1791a47411dd1253af2e5e8ef7c72a)

## Additional Readings
* https://scraperwiki.com/2011/06/why-the-government-scraped-itself/
* http://robertorocha.info/on-the-ethics-of-web-scraping/
* http://opencivicdata.readthedocs.io/en/latest/scrape/basics.html
* http://datajournalismhandbook.org/1.0/en/getting_data_3.html
