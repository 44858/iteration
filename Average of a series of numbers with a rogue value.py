#Lewis Travers
#31/10/2014
#Average of a series of numbers with a rogue value

total = 0
number = 1
count = 0

while number > 0:
    number = int(input("Please enter a number. If you are finished, enter -1: "))
    count = count + 1
if number > 0:
    total = total + number
    total1 = total // count
print(total)
