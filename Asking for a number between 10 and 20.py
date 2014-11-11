#Lewis Travers
#31/10/2014
#Asking for a number between 10 and 20

number = int(input("Please enter a number between 10 and 20: "))

while number <10 or number >20:
    print("That is not within the correct range")
if number >10 and number <20:
        print("That number is within the correct range.")
