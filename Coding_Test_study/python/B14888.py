n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
minN = int(1e9)
maxN = int(-1e9)

def f(c, v):
    global minN, maxN

    if c == n:
        if minN > v: minN = v
        if maxN < v: maxN = v
    else:
        for i in range(4):
            if op[i] == 0: continue

            op[i] -= 1
            if i == 0: f(c+1, v + num[c])
            elif i == 1: f(c+1, v - num[c])
            elif i == 2: f(c+1, v * num[c])
            elif i == 3: f(c+1, int(v / num[c]))
            op[i] += 1

f(1, num[0])
print(maxN)
print(minN)
