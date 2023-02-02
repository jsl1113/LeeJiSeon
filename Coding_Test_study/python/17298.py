import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
result = [-1 for i in range(n)]
l = []

for i in range(n):
    while l:
        if arr[l[-1]] < arr[i]:
            result[l.pop()] = arr[i]
        else:
            l.append(i)
            break
    if not l:
        l.append(i)

print(*result) # 공백 기준 리스트 원소 출력

