#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re 
def function(text):
    return re.search('^[a-z]+_[a-z]+$', text)


x = input()
if function(x):
    print('YES')
else:
    print('NO')