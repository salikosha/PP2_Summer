#Write a Python program to split a string at uppercase letters.
import re
a = input()
result = re.findall("[A-Z][^A-Z]*", a)
print(result)