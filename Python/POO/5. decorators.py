##Functions are the base of decorators.
##metaprogramming is when one piece of code attempts to modify
##another at compile time.
##Thats how decorators work.

##This is how you create a decorator
def decorator_function(function):
	def wrapper():
		print("this is a message")
		function()
		print("this is a new message :)")
	return wrapper

def buzz_function():
	print("Buzzzzzz")

##This could be an integration
buzz = decorator_function(buzz_function)

##To integrate/invoke a decorator in python you have to use @ and the
##name of the decorator function right before the function creation

@decorator_function
def buzz_function():
	print("Buzzzzzz")

buzz_function()