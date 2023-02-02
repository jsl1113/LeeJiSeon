import sys

n = int(sys.stdin.readline())
hill = list(map(int, input().split()))
ans = 0
maxHill = 0
cnt = 0
for h in hill:
    if h > maxHill:
        maxHill = h
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)