#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
x = input()
a = re.search('ab{2,3}', x)
print(a)