from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0 ,-1, 1] #상하좌우

def bfs(i,j):
  global survibe_wolf,survibe_sheep
  que = deque()
  que.append((i,j))
  visited[i][j] = True
  wolf = 0
  sheep = 0
  while que:
    cur_i, cur_j = que.popleft()
    if madang[cur_i][cur_j] == 'v':
      wolf += 1
    elif madang[cur_i][cur_j] == 'o':
      sheep += 1
    for d in range(4):
      new_i = cur_i + di[d]
      new_j = cur_j + dj[d]
      if  0 <= new_i < R and 0 <= new_j < C and madang[new_i][new_j] != '#' and not visited[new_i][new_j]:
        que.append((new_i, new_j))
        visited[new_i][new_j] = True
  if wolf >= sheep:
    survibe_wolf += wolf
  elif wolf < sheep:
    survibe_sheep += sheep

R, C = map(int, input().split())
madang = [list(input()) for _ in range(R)]
visited= [[False] * C for _ in range(R)]
survibe_wolf = 0
survibe_sheep = 0
for i in range(R):
  for j in range(C):
    if madang[i][j] != '#' and not visited[i][j]:
      bfs(i, j)
print(survibe_sheep, survibe_wolf)