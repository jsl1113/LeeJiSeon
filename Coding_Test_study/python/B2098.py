"""
#원소 추가
n = 3
print(bin(0b0010 | (1 << n)))  #  0b1010
#원소 제거
n = 3
print(bin(0b1010 & ~(1 << n)))  #  0b10
#원소 조회
n = 3
print(bin(0b1010 & (1 << n)))  #  0b1000
#원소 토글 (XOR)
n = 3
print(bin(0b1010 ^ (1 << n)))  #  0b10
"""
import sys

def find_path(last, visited):
    visit_all = (1 << n) - 1 # 1111
    if dp[last][visited] != 0:  # 이미 계산되어 있으면
        return dp[last][visited]
    if visited == visit_all:  # 모두 방문했다면
        return w[last][0] or inf

    tmp = inf
    for c in range(n):  # 모든 도시에서
        if visited & (1 << c) == 0 and w[last][c] != 0: # 방문한 적 없고 제자리 걸음이 아니라면
            tmp = min(tmp,
                      find_path(c, visited | (1 << c)) + w[last][c])  # visited | (1 << c) : 원소 추가
    dp[last][visited] = tmp
    return tmp

n = int(sys.stdin.readline())
w = []
inf = sys.maxsize

for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (1 << n) for _ in range(n)]

print(find_path(0, 1 << 0))