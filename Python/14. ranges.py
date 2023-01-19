##Declare a range
my_range = range(1, 5)
print(my_range)
print(type(my_range))

for i in my_range:
    print(i)

my_range2 = range (0, 7, 2)
my_range3 = range (0, 8, 2)

my_range == my_range2               ##We can modify the first range but point it somewhere else

for i in my_range:
    print (i)

print(id(my_range))
print(id(my_range2))

for i in range (0, 101, 2):         ##generate all even numbers from 0 to 100 in orderly fashion
    print(f'pares {i}')

for i in range (1, 100, 2):         ##generate all odd numbers from 1 to 100
    print(f'nones {i}')