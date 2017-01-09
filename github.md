# Git and Github

## Install Git 

### Windows 10
1. Enable [Bash on Ubuntu on Windows](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)
2. Open the "Bash on Ubuntu on Windows"
3. Follow Ubuntu instructions

### Mac
1. Install the [Homebrew](http://brew.sh/) Package Manager
2. Open Terminal, update brew and install git

```
brew update
brew install git
```

### Ubuntu

1. Install Git

```
sudo apt-get install git 
```

## Set up git

```
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR EMAIL ADDRESS"
```

## What is Git?

Keeping track of file versions is hard.
![](http://petapixel.com/assets/uploads/2015/07/psdrevisioning.jpg)

#### So what is Git, and why does it help us?
Above all else, Git is a fast and **distributed** version control system, that allows you to efficiently handle projects large and small.

Here are some problems we face as developers, and how git solves them:

#### Reverting to past versions

Git allows us to make save points at any time. These save points are called 'commits'. Once a save point is made, it's permanent, and allows us to go back to that save point at any time. From there, we can see what the code looked like at that point, or even start building off that version.

#### Keeping track of what each version 'meant'

Every commit has a description (commit message), which allows us to describe what changes were made between the current and previous commit. This is usually a description of what features were added or what bugs were fixed.

Additionally, git supports tagging, which allows us to mark a specific commit as a specific version of our code (e.g. '2.4.5').

#### Comparing changes to past versions

It's often important to see content of the actual changes that were made. This can be useful when:

* tracking down when and how a bug was introduced
* understanding the changes a team member made so you can stay up-to-date with progress
* reviewing code as a team for correctness or quality/style

Git allows us to easily see these changes (called a `diff`) for any given commit.

#### Fearlessness in making changes

In developing software, we often want to experiment in adding a feature or
refactoring (rewriting) existing code. Because git makes it easy to go back to a
known good state, we can experiment without worrying that we'll be unable to
undo the experimental work.

#### Three components of a git repository

1. The working directory
  - `git init` creates a git repo inside current working directory
  - `git init name_of_repo` creates a new folder and a git repo inside that
  - `git status`
2. The staging area
  - `git add .` adds changes from the working directory to the staging area
  - `git add <filename>` adds changes to filenames specified from the working directory to the staging area
3. The repo or commit
  - `git commit -m "commit message"` adds changes in staging area to the repository
  - `git log` shows

Section borrowed from [AlJohri](https://github.com/AlJohri/DAT-DC-12/blob/master/notebooks/intro-git.ipynb)

## Try It (Together)

1. Initialize a git repo inside your `python-playground/` folder.
2. Add each file as a separate commit.
4. Show me the git log

## Try It

1. Initialize a git repo inside your `myname-simple-website/` folder (where `myname` is your first name)
2. Commit the "hello world" webpage
3. Add a heading and paragraph tag

	```
	<!DOCTYPE html>
	<html>
	<body>
	
	<h1>Hello,World</h1>
	<h2>My First Subheading</h2>
	
	<p>My first paragraph.</p>
	
	</body>
	</html>
	```
3. Commit this with a meaningful commit message.
4. Show me the git log

## Branching

See Branches

```
git branch
```

Create a new Branch

```
git checkout -b <branchname>
```


Delete Branches

```
git branch -D <branchname>
```

More on Branches

http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade-2#/4/13

## Try It (Together)
1. in `python-playground/` create a new branch called `add-comments`
2. make sure you're on that branch
2. open up your hello world script
3. add a comment before each line of code
4. commit the change in your new branch
5. notice how this change doesn't exist in your "master" branch.

### Branches IRL (In Real Life)

Branches are frequently used to develop features on a project. People can work independently in branches and then issue a pull request back into master. That pull request is reviewed and merged into the branch.

Branches in one of our projects

[https://github.com/fivethirtyeight/general-forecast](https://github.com/fivethirtyeight/general-forecast)

https://projects.fivethirtyeight.com/2016-election-forecast/

Branches in a public repository

[https://github.com/18F/web-design-standards](https://github.com/18F/web-design-standards)

### Pull Requests (from branch)

For example #471, 468, 461 in #general-forecast

## Try It 
1. in `myname-simple-website/` create a new branch called `linkedin-link`
2. in this new branch, put a link to your linked in page at the bottom  of your simple website

	```
	<a href src="https://www.linkedin.com/in/dhrumilmehta">  find me on linked in! </a>
	```

3. commit the change to the branch

## Git, Conceptually

Under the Hood:

* [https://www.sbf5.com/~cduan/technical/git/](https://www.sbf5.com/~cduan/technical/git/)

How it works:

* [https://cs61.seas.harvard.edu/wiki/2012/Git](https://cs61.seas.harvard.edu/wiki/2012/Git)
* [http://www.eecs.harvard.edu/~cs161/resources/git.html](http://www.eecs.harvard.edu/~cs161/resources/git.html)

Git for Knowledge Workers:

* [https://git-scm.com/video/what-is-version-control](https://git-scm.com/video/what-is-version-control)
* [https://git-scm.com/video/quick-wins](https://git-scm.com/video/quick-wins)

Additional Resources:
	
* [http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade-2#/4/21](http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade-2#/4/21)

## Git, for things other than code
* Auditing system for changes on a file
* For collaboratively editing a text document
* [For drafting government web design standards!](https://github.com/18F/web-design-standards)
* [Drafting](https://github.com/twitter/innovators-patent-agreement) and [collaborating on](https://github.com/twitter/innovators-patent-agreement/issues) legal documents

## Github and Open Source
https://government.github.com/
https://government.github.com/community/

## Tour of Github.com

http://github.com/dmil/

* Your Github Page
* Social Features

## Set up SSH Keys
### Setting up the keys for GitHub

Follow these instructions. Remember, if you're using "Bash on Ubuntu on Windows" then use the "linux" instructions.
[https://help.github.com/articles/generating-an-ssh-key/](https://help.github.com/articles/generating-an-ssh-key/)

### What is SSH?

Videos:

* [What is SSH](https://www.youtube.com/watch?v=zlv9dI-9g1U)
* [Cryptography 101](https://www.youtube.com/watch?v=fNC3jCCGJ0o)
* [What is Cryptography](https://www.youtube.com/watch?v=68Pqir_moqA)

Images below sourced from [David Brumly at Carnegie Mellon University](https://www.youtube.com/watch?v=fNC3jCCGJ0o)

![](https://www.evernote.com/shard/s150/sh/ceba42f8-128c-478b-b857-2b033294a4df/f70388b235260b5a/res/6eaede67-b674-4c28-9306-5b8414d849ae/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/a5150f27-e630-48fb-8794-a1342cfe5076/0c664f25dd396804/res/51319142-13b1-45cd-af94-1cb7177b5bda/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/d2a42614-b368-4536-ada4-f2f641832ec9/b13ba0462deb7322/res/bb33443a-bfe6-4002-b98a-d0aa87c73bf9/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/5614e630-0ea0-4a55-ba14-cf679593fee6/99133c73ac3eca6f/res/30c2aa9c-6fe1-4fae-b8ff-d5b631209b99/skitch.png?resizeSmall&width=832)


#### Key Terms
* **github** - a service that hosts git remote repositories, and provides a web app to interact / collaborate on them
* **remote** - another repository that can be syncronized with a remote
* **upstream** - the name for a remote read-only repository
* **origin** - the name for a remote read-and-write repository
* **clone**  - download an entire remote repository, to be used as a local repository
* **fetch**  - downloading the set of changes (commits) from a remote repository
* **pull**   - fetching changes and merging them into the current branch

## Try It (together)
1. Create a blank github repo for your `python-playground`
2. Set the remote on your local repo to this new repo on github
3. Push your repo up to github


## Try It
1. Create a blank github repo for your `dhrumil-simple-website`
2. Set the remote on your local repo to this new repo on github
3. Push your repo up to github

## Try It
http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade-2#/4/10

## Serving static websites from GitHub

Together we will go through how to serve up your simple website.

## Try It

1. Create a "github page" for yourself
2. (optional) - buy a domain for yourself at [http://namecheap.com](http://namecheap.com). When we get to the "DevOps" lesson, you'll learn how to connect your new domain to either a static or dynamic webpage.

## Forking

Draw on the board, forking vs branching

http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade-2#/4/17

### Key Terms

* **fork** - make a copy of a remote repo on github.
* **merge**  - taking two histories, merge one into the other
* **push**   - sending changes to a remote repository and merging them into the specified branch
* **pull request** - ask the upstream maintainer to pull in changes from origin.
* **merge conflict** - when two commits conflict, and thus can't be merged automatically

## Try It (together)

1. Fork my simple webste (dhrumil's)
2. Assign everyone a number
3. put a link to your simple website next to your number
4. Issue a pull request back to me from your fork.

## Try It

1. Find another partner, and fork their simple webpage.
2. Put an endorsement on their webpage but this time via a fork as if you were an open source collaborator (outside of their organization).

## Pull requests from a fork

### Open source collaboration.

https://github.com/tj/git-extras/pull/356

### Backbone forms example

Github Issue

https://github.com/powmedia/backbone-forms/issues/537

Pull Request (From a Fork)

https://github.com/powmedia/backbone-forms/pull/538

# Homework

Spend at least two hours reading selections from the following reading list. Some of the selections are required, others are optional. Required selections are marked as such. This should not be the end of your reading, this list is just a place to begin. Once you've done some general reading, focus your reading on the issue that your group has been assigned to debate.


## Artifacts
1. Slack channel for your debate group
2. An outline of your opening arguments for tomorrow
3. A list of personal questions or disucssion points for tomrrow about anything your reading, not limited to your debate group.


## Reading List
What is open source?

* Wikipedias
    * https://en.wikipedia.org/wiki/Open-source_model
    * https://en.wikipedia.org/wiki/Open_source_(disambiguation)
    * https://en.wikipedia.org/wiki/Open-source_software_development#Model
* Open Source Intro / Philosophy
    * http://www.dreamsongs.com/IHE/IHE-27.html
    * https://opensource.org/osd
* Open vs Free
    * https://www.gnu.org/philosophy/open-source-misses-the-point.en.html
    * https://www.ubuntu.com/about/about-ubuntu/our-philosophy
    * https://web.kamihq.com/web/viewer.html?state=%7B%22ids%22%3A%5B%220B69u3oA7bfllZFRBdzFvNmk1M0k%22%5D%2C%22action%22%3A%22open%22%2C%22userId%22%3A%22108443026002436873308%22%7D&filename=s00481ed1v01y201302wbe005.pdf - chapter 7
FLOSS/FOSS in Government
* DOD
    * http://dodcio.defense.gov/Open-Source-Software-FAQ/#Defining_Open_Source_Software_.28OSS.29
* Whitehouse
    * https://www.whitehouse.gov/blog/2016/03/09/leveraging-american-ingenuity-through-reusable-and-open-source-software
    * https://sourcecode.cio.gov/
    * https://www.whitehouse.gov/sites/default/files/omb/memoranda/2016/m-16-12_1.pdf
* HHS
    * https://www.hhs.gov/open/2016-plan/open-source-software.html
* 18F
    * https://18f.gsa.gov/2015/01/16/open-source-for-good-government/
    * https://github.com/18F/open-source-policy/blob/master/policy.md
* House
    * http://opengovfoundation.org/open-source-software-now-permitted-in-the-u-s-house-of-representatives/
    * https://www.wired.com/2016/08/open-source-won-now/
* USDS
    * https://playbook.cio.gov/#introduction
    * https://medium.com/the-u-s-digital-service/an-improbable-public-interest-start-up-6f9a54712411#.14y9p9fqd
* Writings of Aaron Swartz
    * http://www.aaronsw.com/weblog/usefultransparency
    * http://crookedtimber.org/2012/07/03/a-database-of-folly/
* Ethics
    *  [Senate ethics code of conduct summary - ("gifts" page)](http://www.ethics.senate.gov/public/index.cfm/files/serve?File_id=1aec2c45-aadf-46e3-bb36-c472bcbed20f)
    * [House Ethics - Gifts](https://ethics.house.gov/gifts/house-gift-rule)
    * [White House Open Source Policy](https://sourcecode.cio.gov/)
    * [Open Source Software in House Press Release](http://congressionaldata.org/open-source-software-now-permitted-in-the-u-s-house-of-representatives-2/)
    * https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/
* Technology-Spending in Congress
    * http://opengovfoundation.org/counting-up-congressional-technology-spending-for-2014-the-u-s-senate/
    * http://opengovfoundation.org/counting-up-congressional-technology-spending-for-2014-the-u-s-house/
    * https://opengovfoundation.org/why-congressional-technology-spending-matters-and-how-to-improve-the-situation/


non-us

* https://www.gov.uk/service-manual/technology/working-with-open-standards
* https://www.gov.uk/service-manual/making-software/open-source.html
* http://meity.gov.in/content/free-and-open-source-software
* https://hackerone.com/resources/hack-the-pentagon
* https://timreview.ca/article/130
* https://www.wired.com/2013/04/openstack-india/

Github and Hiring

* https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/

## Assignment

Tomorrow we will be joined by Seamus Kraft, Director of the Open Gov Foundation and an advocate for open source technology and transparancy in congress. You will be debating Seamus on why congress should be adopting open source software. Seamus will be playing the role of resisting open source software, bringing up the many arguments that he has encountered as to why open source ought not be allowed.

In your groups, you will prepare an outline that goes through the reasons why open source should not be adopted. Each group will focus on a different area. Example areas include:

1. The Business Case for Open Source, cost effectiveness
2. Open Source Software and Security
3. Specialization of Software
4. Maintainance of Open Source Software
5. Ethics of "free work"

You may find other areas to focus your argument, just make sure to check in with the instructor to ensure that there is no overlap. 

Each group will make their opening arguments to Seamus for why a congressional office ought to adopt open source software. He will then engage in a debate with each group and we will then open the discussion to the class and explore each of these areas together.

### Notes

We will be using git and github every day for the remainder of the class. If you feel that you need to reinforce the larning from today to make sure that goes smoothly for you, feel free to spend some time following a git tutorial or reading one of the resources provided during the lesson about git. This one is a great place ot start. [https://try.github.io](https://try.github.io/)

