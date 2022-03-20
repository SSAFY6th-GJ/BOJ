from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    tmp_s = 0
    queue = deque(virus)
    while queue:
        if tmp_s == S:
            break
        for _ in range(len(queue)):
            covid, r, c = queue.popleft()

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = arr[r][c]
                        queue.append((arr[nr][nc], nr, nc))
        tmp_s += 1


    return arr[X - 1][Y - 1]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 바이러스 저장
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            virus.append( (arr[i][j], i, j))
virus.sort()
S, X, Y = map(int, input().split())  # X 랑 Y  -1 하기

print(bfs())