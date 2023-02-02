import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
negative = []
positive = []
ans = 0

for a in arr:
    if a <= 0:
        negative.append(a)
    elif a == 1:
        ans += 1
    elif a > 1:
        positive.append(a)
negative.sort()
positive.sort(reverse=True)

for i in range(0,len(negative), 2):
    if i+1 < len(negative):
        ans += negative[i] * negative[i+1]
    else:
        ans += negative[i]

for i in range(0,len(positive), 2):
    if i+1 < len(positive):
        ans += positive[i] * positive[i+1]
    else:
        ans += positive[i]

print(ans)