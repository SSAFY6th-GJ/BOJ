from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append((i, j))
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = arr[r][c] + 1
                    queue.append((nr, nc))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bfs(0, 0)
res = -9999
is_zero = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            is_zero = True
        res = max(res, arr[i][j])
if is_zero == True:
    print(-1)
elif res == -1:
    print(0)
else:
    print(res - 1)