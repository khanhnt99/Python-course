f = open("big.data", mode="rt")
first10 = []
count = 0
for i in f:
    if count == 10:
        break
    first10.append(i)
    count = count + 1
f.close()

print(first10, len(first10))
