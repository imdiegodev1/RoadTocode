
x = ["Now","this","is","a","list"]		##Declare a list
print(x)

print(len(x))							##Size of the list

print("this" in x)						##Find an element in the list

print(x[2])								##Chose one or many elements of the list
print(x[1:3])

x.append("ok?")							##Add a new element at the end of the list
print(x)

x.insert(0,"Hey!!")						##Add an element in a certain position
print(x)

x.remove("Hey!!")						##Remove an element of the list
print(x)

x.pop(5)								##Remove an element depending on its position
print(x)
