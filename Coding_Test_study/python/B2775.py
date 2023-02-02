def f(floor, num):
    flr = [i for i in range(1, num+1)]
    for i in range(floor):
        for j in range(1, num):
            flr[j] += flr[j-1]
    return flr[-1]

t = int(input())
for _ in range(t):
    floor = int(input())
    num = int(input())
    print(f(floor, num))
