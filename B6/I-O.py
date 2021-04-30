with open("big.data", mode="rt") as f:
    first10 = []
    count = 0

    for i in f:
        if count == 10:
            break
        first10.append(i)
        count = count + 1
    print(f.closed)
print(len(first10))
print(f.closed)
