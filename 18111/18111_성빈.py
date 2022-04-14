import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
# print(map)
time = 0
minV = 256
maxV = 0
# print(a)
# 제일 낮은 땅, 제일 높은 땅 구하기
for i in range(n):
    for j in range(m):
        if map[i][j] < minV:
            minV = map[i][j]
        if map[i][j] > maxV:
            maxV = map[i][j]

# 인벤토리에 땅이 없을 때는 무조건 땅을 최소값에 맞춰서 깎아야함
if b == 0:
    for r in range(n):
        for c in range(m):
            if map[r][c] != minV:
                time += (map[r][c] - minV)*2
    print(time, minV)

# 인벤토리에 땅이 있을때, 최소값에 맞춰서 땅을 깎을때 / 최대값에 맞춰서 땅을 높일때 비교해서 작은 값 출력
# 근데 최대값에 맞춰서 땅을 높이다가 인벤토리에 땅이 0보다 작아지면 무조건 최소값에 맞춰서 깎은 시간으로 출력
else:
    print(maxV, minV)
    mi = 0
    pl = 0
    ## 왜 여기 아래 반복문으로 못들어가는지?????
    for r in range(n):
        for c in range(m):
            # print(map[r][c])
            if not (map[r][c] == minV):
                # time += (map[i][j] - minV) * 2
                pl += (map[r][c] - minV) * 2
            if not (map[r][c] == maxV):
                # b -= maxV - map[i][j]
                # timemax += maxV-map[i][j]
                # if b < 0:
                #     timemax = -1
                mi += maxV - map[r][c]
    print(pl, mi)


    # if timemax > 0:
    #     if timemax > timemin and timemin != 0:
    #         print(timemin, minV)
    #     elif timemax > timemin and timemin == 0:
    #         print(timemax, maxV)
    #     elif timemax <= timemin:
    #         print(timemax, maxV)
    # else:
    #     print(timemin, minV)


