try:     
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")


