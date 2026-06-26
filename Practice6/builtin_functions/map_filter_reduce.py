from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

#map()
squares = list(map(lambda x: x * x, numbers))
print("Map (squares):")
print(squares)

#filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\nFilter (even numbers):")
print(even_numbers)

#reduce()
total = reduce(lambda x, y: x + y, numbers)
print("\nReduce (sum):")
print(total)