from collections import deque
N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]  #숫자가 떨어져있는게 아니고 붙어 있어서 split은 안해줌

di = [-1 ,1, 0, 0]
dj = [0, 0, -1, 1]   #상하좌우

def dfs(i,j):
  que = deque()             #bfs 니까 deque  dfs면 stack
  que.append((i,j))
  while que:
    cur_i, cur_j = que.popleft()
    for d in range(4):
      new_i = cur_i + di[d]
      new_j = cur_j + dj[d]
      if 0 <= new_i < N and 0 <= new_j < M and miro[new_i][new_j] == 1:
        miro[new_i][new_j] = miro[cur_i][cur_j] + 1               # 처음에 함수에 dfs(i,j,count) 이런 식으로 했는데 count 가 너무 높아짐 그래서 이동한 거리만큼 숫자가 나타나게 해야함
        que.append((new_i,new_j))
  return miro[N-1][M-1]

print(dfs(0, 0))