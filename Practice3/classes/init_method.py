class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("sabina", 21)

print(p1.name)
print(p1.age)

class Person:
  pass

p1 = Person()
p1.name = "sabina"
p1.age = 21

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("sabina", 21)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age=21):
    self.name = name
    self.age = age

p1 = Person("sabina")
p2 = Person("aldik", 22)

print(p1.name, p1.age)
print(p2.name, p2.age)


class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("saninka", 21, "Karaganda", "Kazakhstan")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)