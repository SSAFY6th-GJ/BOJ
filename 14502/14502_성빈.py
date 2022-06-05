import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
arr_wall = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

# 바이러스 퍼뜨림
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr_wall[nx][ny] == 0:
                arr_wall[nx][ny] = 2
                virus(nx, ny)
    return

# 안전한 곳 체크
def count():
    check = 0
    for i in range(N):
        for j in range(M):
            if arr_wall[i][j] == 0:
                check += 1
    return check

# 벽 설치
def dfs(cnt):
    global answer
    # 벽이 3개 일 때
    if cnt == 3:
        for i in range(N):
            for j in range(M):
                arr_wall[i][j] = arr[i][j]
        # 바이러스 퍼뜨림
        for i in range(N):
            for j in range(M):
                if arr_wall[i][j] == 2:
                    virus(i, j)
        # 안전한 곳 크기 더 큰 곳 찾기
        answer = max(answer, count())
        return
    # 빈 공간에 벽 설치
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
                dfs(cnt)
                arr[i][j] = 0
                cnt -= 1

dfs(0)
print(answer)



