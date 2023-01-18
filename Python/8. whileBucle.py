x = 0
i = 0

while x <= 1000 and i <= 1000:          ##print all powers from 2 to 1000
    x += 1
    i = 2 ** (x)
    print (i)

day = 0    
week = ['mon', 'thu', 'wen', 'thr', 'fri', 'sat', 'sun']

while day < 7:
   print("today is " + week[day])       ##print days of week
   day += 1