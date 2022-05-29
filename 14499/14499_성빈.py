import sys
input = sys.stdin.readline

# 1 동쪽, 2 서쪽, 3 북쪽, 4 남쪽
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

N, M ,x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [0] * 6

for i in command:
    nx = x + dx[i]
    ny = y + dy[i]

    if not 0 <= nx < N or not 0 <= ny <M:
        continue

    left, right, front, back, top, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if i == 1:
        dice[0], dice[1], dice[4], dice[5] = bottom, top, left, right
    elif i == 2:
        dice[0], dice[1], dice[4], dice[5] = top, bottom, right, left
    elif i == 3:
        dice[2], dice[3], dice[4], dice[5] = bottom, top, front, back
    elif i == 4:
        dice[2], dice[3], dice[4], dice[5] = top, bottom, back, front

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0

    x, y = nx, ny
    print(dice[4])