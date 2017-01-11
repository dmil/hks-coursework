#  Functions

## Defining a function

A function has inputs and an output. The inputs are known as the "arguments", and the output is known as a "return value"

![](https://www.evernote.com/shard/s150/sh/95140bf5-b70e-4fba-93a6-cde487903396/b15f7bf528929e3b/res/51b5407f-b640-4e9a-9c06-4da9f9ada4b4/skitch.jpg?resizeSmall&width=832)

below is an example of a function in python

```
def multiply(a,b):
	return a * b
```

This function takes two arguments (a and b), and returns the value of them multiplied together

![](https://www.evernote.com/shard/s150/sh/9aebfc82-14c3-45db-89d7-d1c5eecc37ba/5a8e9b0d30cdcd0d/res/cc48bfa7-e4e2-449f-8177-a1a9774a13aa/skitch.jpg?resizeSmall&width=832)


##  Calling a function

In the above exercise you have simply defined a function, but you haven't asked python to call it. If you ran the program above, you wouldn't see any output in the terminal.

```
# This part of the code defines a function
def multiply(a,b):
	return a * b

# This part of the code then calls that function and assigns the variable x to its return value
x = multiply(8,9)

# This prints X to the terminal for humans to read
print x
```

## Return vs Print

The function can also contain other logic and do other things. For example, you could write the function above like this:

```
def multiply(a,b):
	print "I'm multiplying two numbers"
	return  a * b
```

This would both print to the terminal and return a value.

## Try It

1. create a new file called `calculator.py` inside your python playground

2. Write a program that defines four functions (multiply, add, subtract, and divide). These functions should not print anything, they should simply perform a mathematical operation on the two arguments and return the value.

4. At the bottom of the file, Call the function and print a line explaining what is happening. Like this:
	
	```
	print "I'm going to multiply 5 and 6"
	x = multiply(5,6)
	print x
	```
	
5. Run the file with the following command:

	```
	python calculator.py
	```

**bonus**

1. Add two more functions, square and cube.
2. Make a function called square_n_times that takes two arguments, number and n. square the number n times and return the result.
