text = "Yooooooooo\nThis is some text\nHave a good one"
text_add = "\nHave a nice day"

with open('test.txt','a') as file:
    file.write(text_add)

