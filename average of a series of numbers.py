#Lewis Travers
#21/10/2014
#Average of a series of numbers

total = 0
number=1
count = 0

while number > 0:
    number = int(input("Please enter a number"))
    count = count + 1
    if number > 0:
        total = total + number
        total = total / count
print(total)
    
