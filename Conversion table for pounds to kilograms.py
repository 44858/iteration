#Lewis Travers
#31/10/2014
#Conversion table for pounds to kilograms

for count in range(1,21):
    kilograms = 1 * count
    pounds = kilograms * 2.2
    print("| {0:^2} | {1:^2} |".format(kilograms,pounds))
