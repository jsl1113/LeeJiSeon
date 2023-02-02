import sys

t = int(sys.stdin.readline())

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    cabbage = [[0] * m for cb in range(n)]
    cnt = 0

    for j in range(k):
        c, r = map(int, sys.stdin.readline().split())
        cabbage[r][c] = 1

    for q in range(n):
        for w in range(m):
            if cabbage[q][w] == 1:
                queue = [[q, w]]
                while queue:
                    fr, fc = queue[0][0], queue[0][1]
                    del queue[0]
                    for x in range(4):
                        ddr = fr + dr[x]
                        ddc = fc + dc[x]
                        if 0 <= ddr < n and 0 <= ddc < m and cabbage[ddr][ddc] == 1:
                            cabbage[ddr][ddc] = 0
                            queue.append([ddr, ddc])

                cabbage[q][w] = 0
                cnt += 1
    print(cnt)
