from collections import deque

def dfs(V):
    visited_dfs[V] = True
    print(V, end=' ')
    for i in arr[V]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(V):
    visited_bfs[V] = True
    queue = deque([V])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in arr[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

visited_bfs = [False] * (N+1)
visited_dfs = [False] * (N+1)
for m in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)            # 양방향향
    arr[y].append(x)

for i in range(1, N+1): # 정점 번호가 작은 것을 먼저 방문
    arr[i].sort()
# arr = [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]
dfs(V)
print()
bfs(V)