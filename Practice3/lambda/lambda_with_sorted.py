students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


cars = [
    {'make': 'Ford', 'model': 'Focus', 'year': 2013},
    {'make': 'Nissan', 'model': 'Versa', 'year': 2015},
    {'make': 'Ford', 'model': 'F-150', 'year': 2011}
]
sorted_cars = sorted(cars, key=lambda car: car['year'])

print(sorted_cars)

colors = ['red', 'white', 'green', 'orange', 'blue']
sorted_colors = sorted(colors, key=lambda s: len(s))

print(sorted_colors)