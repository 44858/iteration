#Lewis Travers
#31/10/2014
#displaying a user's message a given amount of times

message = input("Please enter a message: ")
repeats = int(input("Please enter the amount of times that you would like the message repeated: "))

for count in range(repeats):
    print(message)
    
