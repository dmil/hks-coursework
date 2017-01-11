# APIs

> ... there is software that, using “APIs,”
treats other web sites as just another part of the software infrastructure, another
function it can call to get things done.
Our computers are so small and the Web so great and vast that this last scenario
seems like part of an inescapable trend. Why wouldn’t you depend on other
web sites whenever you could, making their endless information and bountiful abilities
a seamless part of yours? And so, I suspect, such uses will become increasingly common until, one day, your computer is as tethered to the Web as you yourself are
now. 
>
>\- [Swartz: Introduction](http://www.morganclaypool.com/doi/pdf/10.2200/S00481ED1V01Y201302WBE005)


## How Web Apps are Structured

> The other week I made one of my rare excursions from my plushly-appointed bed
and attended a local party. There I met a man who made a website for entering
and visualizing data. I asked him whether he had an API, since it seemed so useful
for such a data-intensive site. He didn’t, he said; it would be too much work to
maintain both a normal application and an API.
>
> I tell you this story because the fellow at the party was wrong, but probably
in the same way that you are wrong, and I don’t want you to feel bad. If even welldressed
young startup founders at exclusive Williamsburg salons make this mistake,
it’s no grave sin.
> 
> See, the mistake is, that if you design your website following the principles
in this book, the API isn’t a separate thing from your normal website, but a natural
extension of it. All the principles we’ve talked about—smart URLs, GET and
POST, etc.—apply equally well to web sites or APIs. The only difference is that
instead of returning HTML, you’ll want to return JSON instead.
>
> \- [Swartz (Chapter 5)](http://www.morganclaypool.com/doi/pdf/10.2200/S00481ED1V01Y201302WBE005)

## Resources

> “The key abstraction of information in REST is a resource. Any information that can be named can be a resource: a document or image, a temporal service (e.g. "today's weather in Los Angeles"), a collection of other resources, a non-virtual object (e.g. a person), and so on. In other words, any concept that might be the target of an author's hypertext reference must fit within the definition of a resource. A resource is a conceptual mapping to a set of entities, not the entity that corresponds to the mapping at any particular point in time.” - Roy Fielding’s dissertation.


## A Case Study

[https://www.crunchbase.com/](https://www.crunchbase.com/)

### Thinking in terms of "Resources"

What are the "Resources" on Crunchbase? (Lets try to map out their database, what do we think it looks like?)

### Thinking about URLs (Uniform Resource Locators)

#### Parts of a URL
[https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)

Additional Resource

[https://doepud.co.uk/blog/anatomy-of-a-url](https://doepud.co.uk/blog/anatomy-of-a-url)
#### What a URL reveals about a web app

> Furthermore, URLs have to last. Those t-shirts and links and blogs will
not disappear simply because you decided to reorganize your server, or move to a
different operating system, or got promoted and replaced by a subordinate (or voted
out of office). They will last for years and years to come, so your URLs must last
with them.
>
>Moreover, URLs do not just exist as isolated entities (like “http://
example.org/lunch/bacon.html”). They combine to form patterns
(“bacon.html”, “lettuce.html”, “tomato.html”). And each of these
patterns finds its place in a larger path of interaction (“/”, “/lunch/”,
“/lunch/bacon.html”).
>
> Because of all this, URLs cannot be some side-effect or afterthought, as
many seem to wish. Designing URLs is the most important part of building a web
application and has to be done first. Encoded in their design are a whole series of
implicit assumptions about what your site is about, how it is structured, and how it
should be used; all important and largely-unavoidable questions.
>
> \- [Swartz (Chapter 2:: Building for Users: Designing URLs)](http://www.morganclaypool.com/doi/pdf/10.2200/S00481ED1V01Y201302WBE005)

## Querying an API

### Client vs Server

![](https://i.stack.imgur.com/Q8T7Z.png)
source: http://stackoverflow.com/questions/11679625/client-vs-server-terminology

![](http://learntocodewith.me/wp-content/uploads/2014/08/client-server.png)
source: http://learntocodewith.me/wp-content/uploads/2014/08/client-server.png

Quick aside about servers, they don't have to look like the strange looking box above. Thre is nothing fundamentally different about a client and a server (both are computers at the end of the day), its just about the roles they play. For example

```
python -m SimpleHTTPServer
```

will immediately make my own computer into a server.

### HTTP Requests

![](http://www.tcpipguide.com/free/diagrams/httprequest.png)
source: [http://www.tcpipguide.com/free/t_HTTPRequestMessageFormat.htm](http://www.tcpipguide.com/free/t_HTTPRequestMessageFormat.htm)

[https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

(open the network tab and view HTTP requests to crunchbase)


### HTTP Verbs (GET vs POST)

![](https://www.evernote.com/shard/s150/sh/0d7425f7-0bf0-4a50-8d98-22e1b939fe8b/3b47367c30172152/res/6c5f88d6-3869-4e0b-873e-1a918718eab5/skitch.png?resizeSmall&width=832)
source: http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/5

### The network tab! (lets explore it for a minute)

### Open the network tab and inspect crunchbase

Lets see if crunchbase is as well structured as it looks! What happens when you load the page for a resource?

https://www.crunchbase.com/person/mark-zuckerberg/

## Another Case Study: The FEC
Browse the Beta FEC website ([https://beta.fec.gov/](https://beta.fec.gov/))

Open the network tab and see how when you get each page, it makes a request to the FEC API.

Now check out the FEC Api that the site is consuming ([https://api.open.fec.gov/developers/](https://api.open.fec.gov/developers/))

Make a database diagram for the FEC API (talk about the word "Model") - talk breifly about MVC.

### Querying the FEC API

#### Try It (together)

#### Try It

#### Try It

- Think about a question you'd want to answer with the FEC API (answering a non-trivial question will probably involve hitting multiple endpoints)
- Think about the endpoints you'd need to hit in order to do this.
- Open a new file called `fec.py` in your `python-playground`

	```
	# I want to get a list of candidates and how much each spent on 
	
	import requests
	
	# Get a list of candidates from georgia by hitting the candidates/ endpoint
	candidates = []
	
	# Loop through all the pages to get a list of candidates
	page = 1
	on_last_page = false
	while !on_last_page:
		url = ""https://api.open.fec.gov/v1/candidates/?api_key=DEMO_KEY&per_page=20&state=GA&sort=name&candidate_status=C&page=" + page
		response = requests.get(url)
		for candidate in response.json():
			candidates.append(candidate)

		page = page+1
	```

	Plan out in the comments each individual step of how you will get the data. You can write a little python too wherever you think you might know how to do the thing needed. Your finished product will look something like what you see above. Write only as much python as you're comfortable with (that may just be `import requests`, that's okay). But try to think through in comments what you would need to do to answer your question. Which endpoints would you have to hit? How would you have to combine the data?
	
	- Push this file to github

## Using APIs (IRL)

* For machines to read data
* Building datasets (not quite the intended use case)

## Other cool APIs

* [https://www.propublica.org/datastore/apis](https://www.propublica.org/datastore/apis)
* [http://elections.huffingtonpost.com/pollster/api](http://elections.huffingtonpost.com/pollster/api)
* [https://developer.nytimes.com/](https://developer.nytimes.com/)

## More about APIs

![](https://www.evernote.com/shard/s150/sh/e700e882-9ada-44b0-8f0e-aef58f2a1f39/bf14351db3d329e4/res/d4b5c513-f127-4268-b312-9af0059a9123/skitch.png?resizeSmall&width=832)

source: [https://www.infoq.com/presentations/API-design-mistakes](https://www.infoq.com/presentations/API-design-mistakes)

## JSON/XML

APIs from Programmable Web till December 2013

![](https://www.evernote.com/shard/s150/sh/d9d3e18e-8209-4ea4-ba3c-dd606a9a88d7/7ff673fe21f09207/res/28b78161-2d50-42e4-bc19-13e9b17c916c/skitch.png?resizeSmall&width=832)
![](https://www.evernote.com/shard/s150/sh/46b2d712-aad5-4098-b28d-5738102147ce/7755ad888bb941fd/res/94b12abb-fc75-496d-97e4-6a4aef5cb952/skitch.png?resizeSmall&width=832)
source: [https://www.infoq.com/presentations/API-design-mistakes](https://www.infoq.com/presentations/API-design-mistakes)

> And so the “Semantic Web Activity” at the Worldwide Web Consortium
(W3C) has spent its time writing standard upon standard...Few have received any widespread use and those that have (XML) are uniformly
scourges on the planet, offenses against hardworking programmers that have
pushed out sensible formats (like JSON) in favor of overly-complicated hairballs
with no basis in reality (I’m not done yet!—more on this in chapter 5).

[Aaron Swartz’s A Programmable Web](https://goo.gl/L21hJQ): Chapter 1 - Introduction: A Programmable Web

>	JSON (pronounced like “Jason”), for the uninitiated, is a simple format for
exchanging basic pieces of data between software. Originally based on JavaScript
but quickly adopted by nearly every major language, it makes it easy to share data
over the Web.

> 	Wait!, you may cry, I thought XML was for sharing data on the Web. Sadly,
you have been misled by a sinister and harmful public relations campaign. XML is
probably just about the worst format for sharing data. Here’s why:


[Aaron Swartz’s A Programmable Web](https://goo.gl/L21hJQ): Chapter 5 - BUILDING A PLATFORM: PROVIDING APIS 
