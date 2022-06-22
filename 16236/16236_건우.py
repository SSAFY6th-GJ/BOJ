from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

level = 2 #상어의 크기
exp = 0  # 상어가 먹은 먹이 개수
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

cur_i = 0
cur_j = 0
def check():
    dist = [[0] * N for _ in range(N)]
    que = deque()
    que.append((cur_i,cur_j))
    while que:
        now_i, now_j = que.popleft()
        for d in range(4):
            new_i = di[d] + now_i
            new_j = dj[d] + now_j
            if 0 <= new_i < N and 0 <= new_j < N and arr[new_i][new_j] <= level and dist[new_i][new_j] == 0:
                dist[new_i][new_j] = dist[now_i][now_j] + 1
                que.append((new_i, new_j))
    return dist

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            cur_i = i
            cur_j = j

answer = 0
while True:
    dist = check()
    go_possible = []
    for i in range(N):
        for j in range(N):
            if 0< arr[i][j] < level:
                if dist[i][j] > 0:   
                    go_possible.append((dist[i][j],i,j))

    if go_possible:
        go_possible.sort()
        d, c, r = go_possible[0]

        arr[cur_i][cur_j] = 0
        answer += d
        cur_i, cur_j = c, r
        arr[cur_i][cur_j] = 0

        exp += 1
        if exp == level:
            level += 1
            exp = 0
    else:
        break
print(answer)
