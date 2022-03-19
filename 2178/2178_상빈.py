from collections import deque

dx = [-1, 0, 1, 0]    # 좌상우하
dy = [0, 1, 0, -1]


Ny, Mx = map(int, input().split())
table = [list(map(int, ' '.join(input()).split())) for _ in range(Ny)]

Q = deque()             # bfs를 위해 deque 사용,
Q.append((0, 0))        # 출발지점(0, 0)을 넣어줌.

while Q:
    y, x = Q.popleft()
    for i in range(4):  # 좌상우하 4방향 모두 탐색
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < Ny and 0 <= xx < Mx and table[yy][xx] == 1:  # 새로운 좌표가 미로를 벗어나지 않았고, 이동 가능할 경우 ( = 1인 경우)
            table[yy][xx] = table[y][x] + 1                       # 기존 좌표의 값 + 1로 변경 후 deque에 추가한다.
            Q.append((yy, xx))

print(table[Ny-1][Mx-1])  # 도착지 값 출력


