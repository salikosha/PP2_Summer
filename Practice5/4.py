#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
def function(txt):
    return re.search("([A-Z]){1}[a-z]+$", txt)
x = input()
print(function(x))