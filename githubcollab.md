# Collaborate in Github


## Review from Yesterday

1. cd into your directory `~/Development/universe`
2. run `pwd` and `ls` to remind yourself where you are and what is there
3. intitialize a git repository in the folder

	```
	git init
	```
4. add all of the files in this folder to the staging area. The way to add all the files rather than one at a time is:
	```
	git add .
	```
5. commit this data with the commit message "create a folder structure that represents the universe"
	```
	git commit -m "create a folder structure that represents the universe"
	```
6. do a `git log` to make sure you committed properly and a `git status` to make sure there are no new changes
7. Create a [blank github repo](https://github.com/new) called "universe"
8. set your remotes (follow the instructions in the new github repository)  
9. check out your repository by refereshing the page in github
















3. open up your `calculator` script and add a comment before the main part of the code that calls the function.
	
	```
	def multiply(x,y):
		return x*y
		
	def add(x,y):
		return x+y
		
	def subtract(x,y):
		return x-y
		
	def divide(x,y):
		return x/y
		
	# This calculator is currently set to print  what it is doing and then multiply two numbers.
	print "I'm going to multiply 5 and 6"
	x = multiply(5,6)
	print x	
	```

