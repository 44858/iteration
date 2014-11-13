#Lewis Travers
#11/11/2014
#Iteration spotcheck question 3

guessed = False
number = 
turns = 0

while guessed == False:
    turns = turns + 1
    user_guess = int(input("Enter your guess for the number: "))
    if user_guess == number:
        guessed = True
    elif user_guess > number:
        print("The number you guessed is too high")
    else:
        print("The number you guessed is too low")

print("You took {0} turns to guess the number.".format(turns))
print("The number was: {0}.".format(number))
