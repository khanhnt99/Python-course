class Cat():
    def __init__(self, name, c):
        self.name = name
        self.color = c
    def __str__(self):
        return "Meo: name: {} color: {}".format(self.name, self.color)
miu = Cat('Miu', 'pink')
print(miu, type(miu))
print(type(miu))
print(miu.name, miu.color)
