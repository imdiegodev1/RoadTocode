#It is when you want to compare two or more elements
a = 33
b = 200

if b > a:
  print("b is greater than a")

##You can compare two elements ith different conditions
if b > a:
  print("b is greater than a")
elif a == b:                        ##The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
  print("a and b are equal")
else:                               ##The else keyword catches anything which isn't caught by the preceding conditions
  print("a is greater than b")

