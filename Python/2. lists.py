my_list = [1,2,3]         ##Define a list
print(my_list[0])         ##Call an element

print(my_list[1:])        ##Call a series of elements depending on its position

my_list.append(4)         ##Add an element to the end of the list
print(my_list)            ##Print all the list

my_list[0] = 'a'          ##Modify the list
print(my_list)

my_list.pop()             ##delete the las value of the list
print(my_list)

list_a = [1,2,3]
b = list_a

print(id(list_a))        ##Carefull, two items are targeting the same element
print(id(b))             

c = [1,2,3]
d = c
e = list(c)               ##Clone a list without targeting the same element
f = c[::]                 ##Other form to clone a list


g = list(range(0, 100, 1))

##List comprenhension
doble = [i * 2 for i in g]              ##Multiply all the elements of the list by a factor of two
print (doble)

pares = [i for i in g if i % 2 == 0]    ##remove even numbers and use the % operator
print(pares)
