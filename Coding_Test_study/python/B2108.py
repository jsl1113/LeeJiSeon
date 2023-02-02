# 산술평균 : N개의 수들의 합을 N으로 나눈 값 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

def mean(num):
    return round(sum(num)/len(num))
def median(num):
    num.sort()
    return num[len(num)//2]
def mode(num):
    mode_dict = Counter(num)  # 딕셔너리로 데이터 등장 횟수 저장
    m = mode_dict.most_common()  # 등장한 횟수를 내림차순으로 정리
    if len(num) > 1:
        if m[0][1] == m[1][1]:
            mod = m[1][0]
        else:
            mod = m[0][0]
    else:
        mod = m[0][0]
    return mod
def scope(num):
    return max(num) - min(num)

print(mean(arr))
print(median(arr))
print(mode(arr))
print(scope(arr))