# Transforming Data

## Data Formats you may encounter

### CSV

"Comma Separated Values"

A simple format that can be viewed in excel. Really easy to see in text editor, contains only one table.

### TSV

"Tab Separated Values"

Same as CSV, but separates values with tabs rather than commas, can also be opened in excel.

### JSON

"JavaScript Object Notation"

Another great Mozilla [tutorial](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

![](https://www.evernote.com/shard/s150/sh/90cf283d-4adc-4f6f-aeaf-c8f2660d13c7/793cabb9f194996b/res/62dd9784-077a-45ee-8b47-c23054e2cc59/skitch.png?resizeSmall&width=832)
source: http://stackoverflow.com/questions/4310315/what-exactly-is-json

Example JSON:
https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json

[Some insane diagrams](http://www.json.org/) that tell you exactly what is valid JSON.

[Validate JSON](http://pro.jsonlint.com/) by pasting into this tool (or many other "linters") online. They will display the data properly and tell you if its valid JSON or not. If it is not valid, you might have trouble reading it into a programming language.

There are also lots of [chrome extensions](https://chrome.google.com/webstore/search/json?hl=en&_category=extensions) to help format json automatically when your browser encounters it. My favorite one (JsonView) apparently has a serious security vulnerability, so DO NOT download it, you can try any of the other ones here though. I've had success with this one  [https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en)

### XML

"eXtensible Markup Language"

We have already spoken eXtensively about these, let me know if you really want to extract XML data.

### PDF

"Portable Document Format"

PDF data is hard to extract. If you have PDFs containing tables, you may be able to copy and paste the tables into a text file or into excel.

I have had success extracting data from PDFs with off the shelf tools when either (1) the PDF contains tables or (2) you have many PDFs that are exactly the same in structure with different data (for example many copies of a form). In these two cases, I'd consider trying
  - http://tabula.technology/
  - https://pdftables.com/

### HTML (data on the webpage)

- Copy/Paste - try this first, sometimes you can just copy an HTML table and paste directly into excel then save as CSV
- import.io (and other [similar tools](https://gist.github.com/cassidoo/9b1791a47411dd1253af2e5e8ef7c72a)) is especially good with extracting tables from websites, but can also extract data from other parts of a website using CSS selectors.

### XLS & XLSX
Excel proprietary data formats - not simple to parse with code. I'd suggest saving tables as CSV and working form there.

## Figuring out what kind of information a visualization takes
 - http://bl.ocks.org/mbostock/4063318
 -

## Tools for dealing with different data formats.

Google is your friend

## CSV to JSON

Much easier than JSON to CSV, lots of tools to do that. Lets explore why...

https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=+csv+to+json

## JSON to CSV

More difficult than going the other way around.

https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=JSON+to+CSV

Lots of default tools to help you do this conversion, many of them work differently so if one doesn't work, try another.

Also, before you drop data into a converter tool, you may have to remove junk/metadata and simplify the JSON.

### Simplifying JSON

#### Using Text editor

* Multi Cursor
* Find and Replace

https://github.com/dzhibas/SublimePrettyJson

#### Console Save & JSON Formatter extension

Chrome extension
https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en

Example data
https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json

lets simplify this data by getting only the "members"

Console Save command
https://coderwall.com/p/prhwzg/add-console-save-to-chrome

First run the snippet (you have to do this every time). Then you can manipulate the JSON in JavaScript in the browser and save the simplified version.

```
console.save(json.members)
```

## Command line tools & Text editor

Be scrappy with your command line tools (like grep) or with your text editor and tools like "find and replace" using regex.

## Regular Expressions Examples

--> Whitehouse Example

--> Examples from the class?

## I CAN HELP!
If you find one format for the final project and need to convert to another, but don't know how - reach out to me early! I can help, especially while I'm still on campus.
