import sys
print(sys.argv)
ns = [int(i) for i in sys.argv[1:]]
print(sum(ns))


