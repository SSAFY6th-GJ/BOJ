from collections import deque

def dfs(v):
  st = [v]
  res = []
  while st:
    cur_pos = st.pop()
    visited[cur_pos] = True
    if cur_pos not in res:
      res.append(cur_pos)
    for j in range(len(graph_dfs[cur_pos])):
      # next_pos = graph[cur_pos][j]
      if not visited[graph_dfs[cur_pos][j]] :
        st.append(graph_dfs[cur_pos][j])
      
  return res

def bfs(v):
  que = deque()
  que.append(v)
  res = []
  while que:
    cur_pos = que.popleft()
    visited[cur_pos] = True
    if cur_pos not in res:
      res.append(cur_pos)

      for j in range(len(graph_bfs[cur_pos])):
        if not visited[graph_bfs[cur_pos][j]] :
          que.append(graph_bfs[cur_pos][j])
  return res

N, M , V = map(int, input().split())
graph_dfs = [[] for _ in range(N+1)]
graph_bfs = [[] for _ in range(N+1)]
for _ in range(M):
  i, j = map(int, input().split())
  graph_dfs[i].append(j)
  graph_dfs[j].append(i)
  graph_bfs[i].append(j)
  graph_bfs[j].append(i)

for k in range(N+1):
  graph_dfs[k].sort(reverse=True)
  graph_bfs[k].sort()

visited = [False for _ in range(1+N)]
print(*dfs(V))
visited = [False for _ in range(1+N)]
print(*bfs(V))
