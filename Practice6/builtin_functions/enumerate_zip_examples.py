#enumerate()

fruits = ["apple", "banana", "orange"]

print("Enumerate:")

for index, fruit in enumerate(fruits):
    print(index, fruit)


#zip()

names = ["Ali", "Dana", "Tom"]
grades = [95, 88, 76]

print("\nZip:")

for name, grade in zip(names, grades):
    print(name, grade)


#Type checking and conversions

x = "100"

x = int(x)
print("\nint():", x)
print("Type:", type(x))

x = float(x)
print("\nfloat():", x)
print("Type:", type(x))

x = str(x)
print("\nstr():", x)
print("Type:", type(x))