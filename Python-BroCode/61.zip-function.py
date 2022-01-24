# zip(*iterable) = aggregate elements from two or more iterables (list, tuple, set)
#                  creates a zip object with paired elements stored in tupples for each elements

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

# users = list(zip(usernames, passwords))
# users = dict(zip(usernames, passwords))
# print(type(users))

# for key,value in users.items():
    # print(key +" : "+value)

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)