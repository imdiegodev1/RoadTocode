##ejercicios con listas
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4))

##Crear una lista con un ciclo

multiplos =[]
for x in range(1,11):
    multiplos.append(x*7)
print (multiplos)

otro_multiplo = [x*5 for x in range(1,11)]
print (otro_multiplo)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(Jamies_list[::-1])

def squares(start, end):
	numbers = []
	r
	return [ ___ ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]