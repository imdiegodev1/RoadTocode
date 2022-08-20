x = "Hello World"               ##Declare a string

letter = x[0]                   ##Get a character of the string specifying its position

length = len(x)                 ##Length of the string

check = "hello" in x            ##Check if a word or letter is in string (case sensitive)

check2= "cat" not in x          ##Check if a word or letter is not in string (case sensitive)

y = x +" "+"This is a test"     ##Concatenating strings

##Slicing a string
first_word = x[:5]

last_word = x[6:]

last_letter = x[-1]

##Modify string
upper_case = x.upper()

lower_case = x.lower()

remove_space = x.strip()

replace_part = x.replace("H", "J")  ##Case sensitive

split = x.split(" ")            ##Define the character you want to use to split. Returns a list.

