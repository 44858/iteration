#Lewis Travers
#10/10/2014
#Converting ASCII code into text characters

ascii_text = input("To enter an ASCII code, input 'ascii'. To enter a character, input 'text'")


if ascii_text == 'ascii':
    ascii_code = int(input("Please enter an ASCII code: "))
    print("The character equivalent is {0}.".format(chr(ascii_code)))
elif ascii_text == 'text':
    character = input("Please enter a character:")
    print("The ASCII code equivalent is {0}.".format(ord(character)))


    
