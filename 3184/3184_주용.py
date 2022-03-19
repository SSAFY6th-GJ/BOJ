# 답은 아님
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r,c):
    global total_wolf, total_sheep
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    # 울타리 안에 있는 늑대와 양 세기
    wolf = 0
    sheep = 0
    if arr[r][c] == 'v':
        wolf += 1
    elif arr[r][c] == 'o':
        sheep += 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != '#' and visited[nr][nc] == False:
                if arr[nr][nc] == 'v':
                    wolf += 1
                elif arr[nr][nc] == 'o':
                    sheep += 1
                visited[nr][nc] = True
                queue.append((nr, nc))

    # 늑대와 양이 최소 1개 이상 있을때만 적용
    if wolf > 0 and sheep > 0:
        if wolf > sheep:
            total_sheep -= sheep
        else:
            total_wolf -= wolf

R, C = map(int, input().split())
arr = [list((input())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
# 일단 전체 늑대와 양의 수를 세기  ---- 시작
total_wolf = 0
total_sheep = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'v':
            total_wolf += 1
        elif arr[i][j] == 'o':
            total_sheep += 1
# 일단 전체 늑대와 양의 수를 세기  ---- 끝
for i in range(R):
    for j in range(C):
        if (arr[i][j] == 'v' or arr[i][j] == 'o') and visited[i][j] == False:
            bfs(i, j)
            visited[i][j] = True
print(total_sheep, total_wolf)