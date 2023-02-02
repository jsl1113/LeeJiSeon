import sys

n = int(sys.stdin.readline())
L = []
for i in range(n):
    L.append(list(map(int, sys.stdin.readline().split())))
L.sort(key=lambda x:(x[1], x[0]))

for l in L:
    print(l[0],l[1])