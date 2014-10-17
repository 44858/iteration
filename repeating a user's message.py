#Lewis Travers
#17/10/2014
#Repeating a user's message

message = input("Please enter a message")

repeats = int(input("Please enter the amount of times that you would like the message to be repeated"))

for count in range(repeats):
    print(message)
