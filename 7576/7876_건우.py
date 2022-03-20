from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():
  que = deque(good_tomatos)
  count = 0
  while que:
    for _ in range(len(que)):
      cur_i, cur_j = que.popleft()
      for d in range(4):
        new_i = cur_i + di[d]
        new_j = cur_j + dj[d]
        if 0 <= new_i < N and 0 <= new_j < M and box[new_i][new_j] == 0:
          box[new_i][new_j] = 1
          que.append((new_i,new_j))
    count += 1
  return count-1
    


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
good_tomatos=[]
no_good_tomato = 0
for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      good_tomatos.append((i,j))
    elif box[i][j] == 0:
      no_good_tomato += 1

res = bfs()
if no_good_tomato == 0:
  res = 0
for i in range(N):
  for j in range(M):
    if box[i][j] == 0:
      res = -1
      break
print(res)
