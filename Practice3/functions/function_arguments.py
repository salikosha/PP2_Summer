def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")


def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)



def my_function(x, y):
  return x + y

result = my_function(8, 9)
print(result)

def my_function(name):
  print("Hello", name)

my_function(name = "Emil")
