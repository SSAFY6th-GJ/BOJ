
from collections import deque
# 좌상, 좌하, 좌, 상, 우상, 우하, 우, 하,
dr = [-1, 1, 0, -1, -1, 1, 0, 1]
dc = [-1, -1, -1, 0, 1, 1, 1, 0]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        r,c = queue.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 8 and 0 <= nc < 8 and arr[nr][nc] != '#':

arr = [list(input()) for _ in range(8)]
