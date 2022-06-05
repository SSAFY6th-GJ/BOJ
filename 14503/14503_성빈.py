import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽

# 현재 위치와 청소 가능 한지
def dfs(r, c, d):
    global answer
    if arr[r][c] == 0:
        arr[r][c] = 2
        answer += 1
    # 방향 + 3 을 4로 나눈 나머지가 왼쪽 방향임
    for _ in range(4):
        nd = (d+3) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if arr[nr][nc] == 0:
            dfs(nr, nc, nd)
            return
        d = nd
    # 4방향 이동할 수 없을 때 뒤로 이동한다
    nd = (d + 2) % 4
    nr = r + dr[nd]
    nc = c + dc[nd]
    if arr[nr][nc] == 1:
        return
    dfs(nr, nc, d)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
dfs(r, c, d)
print(answer)

