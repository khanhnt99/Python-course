def drink(name, age):
    if age % 2 == 0:
        print("beer")
    else:
        print("Ruou")

def main():
    name = input("Nhap ten: ")
    age = input("Nhap tuoi: ")
    drink(name, age)

if __name__ == "__main__":
    main()
