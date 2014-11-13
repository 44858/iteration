#Lewis Travers
#11/11/2014
#iteration spotcheck question 2
number = int(input("Please enter an integer: "))
for count in range(1,12):
    total = number * count
    print(" {0:>2} * {1:>2} = {2:>2}".format(count, number, total))
