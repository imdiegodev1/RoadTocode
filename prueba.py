#def fractional_part(numerator, denominator):
#	if numerator == 0 or denominator == 0:
#		return 0
#	else:
#		return ((numerator / denominator) - (numerator // denominator))
#
#
#print(fractional_part(5,0))
#
#def sum(x, y):
#	return(x+y)
#print(sum(sum(1,2), sum(3,4)))
#
#
#def format_name(first_name, last_name):
#	if first_name != "" and last_name != "":
#        string = last_name + ", " + first_name
#    elif first_name != "" and last_name == "":
#        string =  first_name
#    elif first_name == "" and last_name != "":
#        string = last_name
#    else:
#        string = ""
#	
#	return string 
#
#print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

#print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

#print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

#print(format_name("", ""))
# Should return an empty string







##Prueba modulo 3

#number = 1
#while number <= 7:
#    print(number, end = " ")
#    number += 1

def show_letters(word):
	for letter in word:
		print(letter)

#show_letters("Hello")


def multiplication_table(start, stop):
	for x in range(1, (start*stop)+1):
		for y in range(1, (stop*start)+1):
			print(str(x*y), end=" ")
		print()

#multiplication_table(1, 3)

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

##votes(['yes','no','maybe'])

def digits(n):
	count = 0
	if n == 0:
	  print(1)
	while (___):
		count += 1
		___
	return count