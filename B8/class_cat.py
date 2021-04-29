class Cat():
    def __init__(self, name, c):
        self.name = name
        self.color = c
        self.gut = []
    def __str__(self):
        return "{}: color {}".format(self.name, self.color)
    def keu(self):
        print("meo meo meo")
    def eat(self, thing):
        self.gut.append(thing)
        print("meo meo ngon ngon vo cung")

#class SuperCat():
#    def __init__(self, name, c):
#        self.name = name
#        self.color = c
#        self.gut = []
#    def __str__(self):
#        return "{}: color {}".format(self.name, self.color)
#    def keu(self):
#        print("Muaahhh")
#    def eat(self, thing):
#        self.gut.append(thing)
#        print("meo meo ngon ngon")
#    def fly(self):
#        print("viu viu viu")
class SuperCat(Cat):
    def fly(self):
        print("viu viu")
    def keu(self): # override
        print('Muaaaah')
#c = Cat('miu', 'white')
#c.keu()
#c.eat("fish")
sc = SuperCat('supercattom', 'dark')
print(sc)
sc.eat('fish')
sc.fly()
sc.keu()
# print(c.gut)


