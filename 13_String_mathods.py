name = "Dhaval Kurkutiya"

 # lower() method converts all the characters in the string to lower case.
print(name.lower())

 # upper() method converts all the characters in the string to upper case.
print(name.upper())

 # title() method converts the first character of each word to upper case.
print(name.title())
 # capitalize() method converts the first character of the string to upper case.
print(name.capitalize())

 # swapcase() method converts the lower case letters to upper case and vice versa.
print(name.swapcase())

# count() method returns the number of occurrences of a substring in the given string.
print(name.count('a'))

# find() method returns the lowest index of the substring if it is found in the string. If its is not found then it returns -1.
print(name.find('a'))

# index() method returns the lowest index of the substring if it is found in the string. If its is not found then it returns ValueError.
print(name.index('a'))

# replace() method replaces the old substring with the new substring.
print(name.replace('a', 'A'))

# split() method splits the string into substrings if it finds instances of the separator.
print(name.split(' '))
print(name.split('a'))

# join() method takes all items in an iterable and joins them into one string.
print(' '.join(name))
print('a'.join(name))
print('a'.join(name.split('a')))
print('a'.join(name.split('a')).split('a'))

# strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
print(name.strip('a'))

# lstrip() method removes any leading characters (space is the default leading character to remove)
print(name.lstrip('a'))

# rstrip() method removes any trailing characters (space is the default trailing character to remove)
print(name.rstrip('a'))

# center() method returns a string which is padded with the specified character.
print(name.center(30, '-'))

# ljust() method returns a left-justified string of a given minimum width.
print(name.ljust(30, '-'))

# rjust() method returns a right-justified string of a given minimum width.
print(name.rjust(30, '-'))

# encode() method returns the encoded version of the string.
print(name.encode())

# expandtabs() method sets the tab size to the specified number of whitespaces.
print(name.expandtabs(2))

# isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print(name.isalnum())

# isalpha() method returns True if all the characters are alphabet letters (a-z).
print(name.isalpha())

# isdecimal() method returns True if all the characters are decimals (0-9).
print(name.isdecimal())

# isdigit() method returns True if all the characters are digits, otherwise False.
print(name.isdigit())

# isidentifier() method returns True if the string is a valid identifier, otherwise False.
print(name.isidentifier())

# islower() method returns True if all the characters are in lower case, otherwise False.
print(name.islower())

# isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
print(name.isnumeric())

# isprintable() method returns True if all the characters are printable, otherwise False.
print(name.isprintable())

# isspace() method returns True if all the characters in the string are whitespaces, otherwise False.
print(name.isspace())

# istitle() method returns True if the string follows the rules of a title, otherwise False.
print(name.istitle())
