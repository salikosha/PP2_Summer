numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))


fruits = ["apple", "banana", "cherry", "kiwi", "grape"]
# Filter out words longer than 5 letters
# The lambda 'len(w) > 5' returns True if the word has more than 5 characters
long_fruits = filter(lambda w: len(w) > 5, fruits)

# Convert the filter object to a list
print(list(long_fruits))


data_list = ["apple", "", None, "banana", 0, "cherry"]
truthy_list = list(filter(None, data_list))

print(truthy_list)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
