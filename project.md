# Project

Data Driven Storytelling

## Product

For your final project, you will work in a scrum-inspired agile software team with your classmates to tell a data-driven story about a particular area of policy interest. Your team will select one or many datasets, and create a web application with two or more interactive graphics that tells a coherent story about your data.

### Selecting Data

You are welcome to select data from any data source, as long as you are able to understand the format that the data is in and transform it into a format that works for the visualization that you would like to build. I would recommend http://data.gov as a place to start.

### Selecting a visualization

As we mentioned in class, [D3JS](https://d3js.org/) (Data Drivien Documents) is not a "charting library", but rather a language in which graphics are written. For this reason there are many examples of D3 graphics out in the wild for you to pull from, and data visualization professionals are adding new ones every day. Find a visualization that does a good job explaining to the reader the point you're hoping to make given the dataset you have selected. Remember, D3 gives you lots of options that include interactivity and creative visualization. Try to select at least one graphic that allows you to display data in a way that would be difficult in excel or another tool that you already use.

### Building a "Back-End"

Since we didn't cover databases, we're not going to have a proper "back end" server that pulls from a database and serves up an API. Rather, you will find a dataset and create a github repo that you will call `final-project-backend`. This repo should contain a folder for each dataset that you work with.

![](https://www.evernote.com/shard/s150/sh/672834fe-6139-4fd4-972f-4ed924dae2e0/4523b8fdf8508891/res/f7f7ba56-e5ca-4f82-ad50-1d371340e393/skitch.png?resizeSmall&width=832)

Each folder will have

- a `README.md` file with a link to the original data source and an explanation about how you transformed the original data into the final format you needed
- a copy of the original data in the format you got it in
- a copy of the final data which will be consumed by the "front end"

You can find example D3 visualizations at the following places, but I'd also encourage you to google around. They're all over the internet!

- http://bl.ocks.org/mbostock (Mike Bostock created D3JS, these are his examples)
- http://bl.ocks.org/ (same website, examples by different people)
- https://d3js.org/
- http://christopheviau.com/d3list/gallery.html
- https://github.com/d3/d3/wiki/Gallery

### Building a "Front-End"

The front end will contain HTML, CSS, and JavaScript.

You're welcome to use a different file structure, however there is an example file structure in the `example-project` repository which I think will serve you well. You are welcome to serve your application in either one page, or on multiple pages with links or buttons to navigate between them.

#### Developing Locally

Please note also that although GitHub pages automatically renders D3 visualization, your computer does not. If you are working locally on your computer you will need to open the folder containing your `index.html` and run

```
python -m SimpleHTTPServer 8000
```

Then you can view your page as you're building it by typing into the address bar in the browser [0.0.0.0:8000](http://0.0.0.0:8000/)

#### Sidenote

One additional side-note about visualizing data in charts. Often a descriptive title and subtitle of the chart (or as we journalists say a "Hed" and "Dek") can go a long way to effectively communicating either the [purpose](https://fivethirtyeight.com/features/trump-isnt-tweeting-about-the-polls-anymore/) or the [content](https://fivethirtyeight.com/features/an-fbi-error-opens-a-window-into-government-demands-for-private-info/) of the data that you are visualizing.

## Process

Remember to keep your processes agile. This means you team will value:

**Individuals and interactions** over processes and tools

**Working software** over comprehensive documentation

**Customer collaboration** over contract negotiation

**Responding to change** over following a plan

### Roles
Appoint a scrum master, a project owner, and team members.

  * The product-owner is in charge of documenting progress on your scrum board in trello every day.
  * The scrum master is in charge of documenting standup meetings.
  * Team members (and the scrum master and product owner) will collaborate using GitHub to build the project together.

### Daily Scrum Meeting

Your team will hold a daily scrum meeting. These stand-up meetings can be as brief or as long as you need, although remember, the scrum meeting is intended to be short and is frequently done standing up for this purpose. You don't have to resolve your problems during scrum, just surface them and resolve them with only the parties that need to be present either online or offline.

Remember, one of the twelve principles of agile development is:

>"The most efficient and effective method of conveying information to and within a development team is face-to-face conversation."
[- 12 Principles Behind Agile Manifesto](https://www.agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/)

Since Agile development prioritizes individuals and interactions over processes and tools, and highly values face to face conversations, the scrum meeting must be either in person or via video conference. If you think video conferences are not working, you can make a quick pivot to in-person meetings.

### User Stories

Once you've selected the subject and have a sense of what types of datasets you will be visualizing, your team will submit at least 6 user stories, you're welcome to submit more if it helps you determine what to build and how to build it. At least three of these user stories will be people who view your application and at least three will be "stakeholders" in this class (including but not limited to yourselves). Please make sure that each member of the team submits one user story from the perspective of themselves, this will help the whole team function better.

>As a ____
>
>I want ____
>
>so that ____.

### Sprint Planning
Your team will hold a sprint-planning meeting at the start of the project period. This meeting will be split into two parts as described in "SCRUM: A Breathtakingly Breif and Agile Introduction". Re-read the section on sprint planning before starting this meeting.

During the first part of the meeting the team will collectively decide how much they think they can accomplish.

During the second part, you will break the stories down into tasks and put them on a trello board. Everyone on the team will assign tasks to themselves. This will involve a round of scrum "poker".

### Sprint Review

https://www.mountaingoatsoftware.com/agile/scrum/meetings/sprint-review-meeting

### Retrospective

https://www.mountaingoatsoftware.com/agile/scrum/meetings/sprint-retrospective

> Using this approach each team member is asked to identify specific things that the team should:
>
> Start doing
>
> Stop doing
>
> Continue doing

### Artifacts

Process

* Maintain an active [task board](https://www.mountaingoatsoftware.com/agile/scrum/scrum-tools/task-boards) on Trello
* You will submit a "burn down" or a "burn up" chart with how many "points" you accomplished each day as a team
* Maintain a record of your collaboration on GitHub using social features such as commenting on one another's code, recording problems with github issues, or leaving notes when merging branches and approving pull requests.
* If you're not meeting in person, I would also expect that your project group would have an active slack channel.
* Some kind of record of your "standup" meetings (perhaps the scrum-master's notes about blockers)

Product

* A `Back End` repository as described in the section above
* A `Front End` repository as described in the section above
* A link to your final project rendered on GitHub pages

(If you want to make the README.md files look nice, just take a look at the raw code behind the file you're currently reading)

## Grading

* 50% process
* 50% product

## Example Charts

https://github.com/dmil/example-charts

## Availability

I am on campus at least Saturday and Sunday and available to meet either in person or via video chat. My office is in "Belfer Lobby 2A" which is located to the right of the Belfer entrance. Just shoot me a message on slack letting me know you're coming and I can arrange to meet you there or can help remotely via slack. After Monday, I can assist with projects remotely, however I will be back at work in New York, so I won't be able to be nearly as responsive until the evenings.

## Final Note
I'm hoping that your projects will not only demonstrate your newly acquired technical abilities, but also will tell a coherent story, advocate for a position, or otherwise communicate an issue in a meaningful way. The project should show that you are able to use these technical skills meaningfully in the context of your policy education.

Best of luck and enjoy! Please feel free to reach out via slack, email (dhrumil.mehta [at] gmail.com), if you have any further questions, comments or concerns.
