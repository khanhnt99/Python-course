x=5
y=7
z=x+y
print("z:{}".format(z))

ns = [1,3,2]
ns.sort()
print("ns",ns)

age = 18
sex='male'
if age < 18:
    print("Chua du tuoi", age)
    print("Moi ve")
elif age == 18:
    print("Tang 1 ban trai")
    print("Moi vao")
else:
    print("Du tuoi", age)
    print("Moi vao")

ns = [2,5,1,4]
for n in ns:
    if n % 2 ==0:
        print(n,n**2)
        print("hihi")
print("Het")

