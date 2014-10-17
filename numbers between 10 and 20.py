#Lewis Travers
#17/10/2014
#asking for a number in between 10 & 20

number = int(input("Please enter a number inbetween 10 and 20: "))

while number < 10 or number > 20:
    print("That is not within the valid range")
    number = int(input("Please enter a number inbetween 10 and 20: "))
if number > 10 and number < 20 :
     print("That is within the correct range")
