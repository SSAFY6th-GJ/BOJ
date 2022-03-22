import sys
# dfs는 재귀 bfs queue 에 nr, nc 넣기
# from collections import deque
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # bfs
# def bfs(r, c, safe):
#     queue = deque()
#     queue.append((r, c))
#     visited[r][c] =  True
#     while queue:
#         r, c = queue.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False:
#                 if arr[nr][nc] > safe:
#                     visited[nr][nc] = True
#                     queue.append((nr, nc))
#
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# max_height = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] > max_height:
#             max_height = arr[i][j]
# for safe in range(max_height):
#     cnt = 0
#     visited = [[False] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > safe and visited[i][j] == False:
#                 bfs(i, j, safe)
#                 cnt += 1
#     if res < cnt:
#         res = cnt
# print(res)

# dfs
sys.setrecursionlimit(10000)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c, safe):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] > safe and visited[nr][nc] == False:
                visited[nr][nc] = True
                dfs(nr, nc, safe)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0
max_height = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_height:
            max_height = arr[i][j]
for safe in range(max_height):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > safe and visited[i][j] == False:
                cnt += 1
                dfs(i, j, safe)
    if res < cnt:
        res = cnt
print(res)