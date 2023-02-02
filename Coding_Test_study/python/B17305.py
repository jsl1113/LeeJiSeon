import sys

N, w = list(map(int, sys.stdin.readline().rstrip().split(" ")))
arr3 = []
arr5 = []
for _ in range(N):
    tmp_arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if tmp_arr[0] == 3:
        arr3.append(tmp_arr)
    else:
        arr5.append(tmp_arr)
arr3 = sorted(arr3, key=lambda x: -x[1])
arr5 = sorted(arr5, key=lambda x: -x[1])

pre_arr3 = [0]
for i in range(len(arr3)):
    pre_arr3.append(pre_arr3[i] + arr3[i][1])

pre_arr5 = [0]
for i in range(len(arr5)):
    pre_arr5.append(pre_arr5[i] + arr5[i][1])

arr3_num = min(int(w / 3), len(arr3))
max_val = 0
while arr3_num >= 0:
    arr5_num = min(int((w - arr3_num * 3) / 5), len(arr5))
    max_val = max(max_val, pre_arr3[arr3_num] + pre_arr5[arr5_num])
    arr3_num -= 1
print(max_val)