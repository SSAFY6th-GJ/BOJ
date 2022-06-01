import sys
sys.stdin = open('연구소.txt')
from collections import deque
import copy
dx = [-1, 1, 0, 0]  # 행
dy = [0, 0, -1, 1] # 열

def bfs():
    global answer
    cnt = 0
    queue = deque()
    tmp_arr = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 2:
                queue.append((i,j))
    while queue:

        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                queue.append((nx, ny))

    for i in range(N):
        cnt += tmp_arr[i].count(0)
    answer = max(answer, cnt)
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
wall(0)
print(answer)