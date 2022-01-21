import os

source = "/home/khanhnt/Git/Python-course/Python-BroCode/test.txt"
destination = "/home/khanhnt/Desktop/test.txt"
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")



