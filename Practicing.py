#today (23.12.2025) I studied how to open files in python. That's actually not that hard, let's try
with open("pythonpractice", "r") as file:
    print(file.read())
    print(file.read(16))
    print(file.read(5))
    print(file.read(9))
    print("first line: " + file.readline())

