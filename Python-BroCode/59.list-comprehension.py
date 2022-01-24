squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,0]

pass_students = list(filter(lambda x: x>=60, students))
passed_students = [i for i in students if i >= 60]
print(pass_students)
print(passed_students)

