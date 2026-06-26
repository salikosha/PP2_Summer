#Write a python program to convert snake case string to camel case string.

import re
a = input()
print(''.join(x.capitalize() for x in a.split('_')))
#The capitalize() method returns a string where 
#the first character is upper case, and the rest is lower case.