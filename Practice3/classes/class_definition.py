class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

class Bike:
    name = ""
    gear = 0
bike1 = Bike()
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear}")