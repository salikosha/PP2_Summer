with open("./Practice6/MyFile.txt", "a") as file:
    file.write("New line 1\n")
    file.write("New line 2\n")

with open("./Practice6/MyFile.txt", "r") as file:
    print(file.read())