import sys
input = sys.stdin.readline

from collections import deque

arr = list(list(input().rstrip()) for _ in range(8))

visited = [[0] * 8 for _ in range(8)]

dx = [0,0,1,-1,1,-1,1,-1,0]
dy = [1,-1,0,0,1,1,-1,-1,0]

q = deque()
q.append((7,0))
visited[7][0] = 1
result = 0
while q:
    x, y = q.popleft()
    if arr[x][y] == '#': # 벽이면 현재 위치에 서있기
        continue
    for k in range(9):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= ny < 8 and 0 <= nx < 8 and arr[nx][ny] != '#' and visited[nx][ny] == 0:
            q.append((nx, ny))
            visited[nx][ny] = 1
            if nx == 0: # 맨 위로 올라가기만 하면 도착가능
                result = 1


print(result)

'''
1초 마다 벽이 아래로 내려오는거 처리를 어떻게 하는지?
'''
