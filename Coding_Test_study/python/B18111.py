import sys
from collections import defaultdict

n, m, b = map(int, sys.stdin.readline().split())
dic = defaultdict(int)  # default값이 int인 딕셔너리

for i in range(n):
    for j in list(map(int, input().split())):
        dic[j] += 1

print(dic)

key = list(dic.keys())
bot = min(key)
top = max(key)
cnt = int(1e9)
h = 0

for x in range(bot, top+1):
    count, have = 0, b
    for y in dic.keys():
        if x > y:
            count += (x - y) * dic[y]
            have -= (x - y) * dic[y]
        elif x < y:
            count += 2 * (y - x) * dic[y]
            have += (y - x) * dic[y]

    if have >= 0:
        cnt = min(cnt, count)
        if cnt == count:
            h = x
print(cnt, h)