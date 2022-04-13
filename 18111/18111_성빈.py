import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
# print(map)
time = 0
minV = 256
maxV = 0
# print(a)
for i in range(n):
    for j in range(m):
        if map[i][j] < minV:
            minV = map[i][j]
        if map[i][j] > maxV:
            maxV = map[i][j]

if b == 0:
    for r in range(n):
        for c in range(m):
            if map[r][c] != minV:
                time += (map[r][c] - minV)*2
    print(time, minV)

else:
    print(maxV, minV)
    m = 0
    p = 0
    ## 왜 여기 아래 반복문으로 못들어가는지?????
    for r in range(n):
        for c in range(m):
            if map[r][c] != minV:
                # time += (map[i][j] - minV) * 2
                p += (map[r][c] - minV) * 2
            elif map[r][c] != maxV:
                # b -= maxV - map[i][j]
                # timemax += maxV-map[i][j]
                # if b < 0:
                #     timemax = -1
                m += maxV - map[r][c]
    print(p, m)


    # if timemax > 0:
    #     if timemax > timemin and timemin != 0:
    #         print(timemin, minV)
    #     elif timemax > timemin and timemin == 0:
    #         print(timemax, maxV)
    #     elif timemax <= timemin:
    #         print(timemax, maxV)
    # else:
    #     print(timemin, minV)


