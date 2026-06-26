#Write a Python program to insert spaces between words starting with capital letters.

import re
a = str(input())
result = re.findall("[A-Z][^A-Z]*", a)
print(' '.join(result))