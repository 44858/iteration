#Lewis Travers
#11/11/2014
#iteration spotcheck question 1d

number = 0
total = 0
while number != -1:
    number = int(input("Please enter a number: "))
    total = total + (number * number)
    if number == -1:
        total = total - 1

print("The total is {0}.".format(total))
