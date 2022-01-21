def hello(**names):
    # print("Hello " + kwangs['first'] + " " + kwangs['last'])
    print ("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")


hello(title="Mr.",first="Bro",middle="Dude",last="Code")