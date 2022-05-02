import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(i,j):
    visited[i][j] = 1
    q = deque()
    q.append([i,j])
    temp= []
    temp.append([i,j])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<= ny < N and visited[nx][ny]==0:

                if L <= abs(map[nx][ny]-map[x][y]) <= R:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp
cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag= False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                temp = bfs(i,j)
                if len(temp) >1:
                    flag=True
                    num = sum(map[x][y] for x,y in temp)//len(temp)
                    for x,y in temp:
                        map[x][y] = num
    if cnt == False:
        break
    cnt += 1

print(cnt)