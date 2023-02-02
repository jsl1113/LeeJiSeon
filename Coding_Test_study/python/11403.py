import sys

n = int(sys.stdin.readline())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1 or (g[i][k] == 1 and g[k][j] == 1):
                g[i][j] = 1

for r in g:
    for c in r:
        print(c, end=" ")
    print()
