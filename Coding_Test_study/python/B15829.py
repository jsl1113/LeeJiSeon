a, b, v = map(int, input().split())
day = 0
high = v-a
if high % (a-b) == 0:
    print(int(high/(a-b)) + 1)
else:
    print(int(high/(a-b) + 1) + 1)