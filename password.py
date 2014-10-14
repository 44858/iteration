#Lewis Travers
#14/10/2014
#Password exercise

password = ""
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print("You now have access to the system.")
    else:
        print("You have entered the incorrect password, please try again")
