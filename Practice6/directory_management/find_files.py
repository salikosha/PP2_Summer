import os
#Find txt in Folder1
for file in os.listdir("./Folder1"):
    if file.endswith(".txt"):
        print(file)