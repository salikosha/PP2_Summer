import os

if os.path.exists("./Practice6/MyFileCopy.txt"):
    os.remove("./Practice6/MyFileCopy.txt")
    print("File deleted.")
else:
    print("File not found.")