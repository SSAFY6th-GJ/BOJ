from collections import deque   # deque는 list랑 비슷하지만 앞이나 뒤에 자유롭게 빼올수 넣을수 있다.
dr = [-1, 1, 0, 0] # 행으로 상 하 좌 우
dc = [0, 0, -1, 1] # 열으로 상 하 좌 우

def bfs(r,c):
    queue = deque() # queue로 이름을 만든다
    queue.append((r,c)) # 시작 (행, 열) 넣기
    while queue:
        r, c = queue.popleft()
        for i in range(4):      # 상하좌우 좌표 뽑아내기
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M or arr[nr][nc] == 0: # 배열에서 벗어나면 continue
                continue
            else:
                if arr[nr][nc] == 1:        # 상하좌우 봤을때 1이 있다? 그러면
                    arr[nr][nc] = arr[r][c] + 1     # 이전꺼에 1을 계속해서 더해주는 방식으로 만들어나가기
                    queue.append((nr, nc))          # 또 상하좌우 탐색하기
    return arr[N-1][M-1]        # 원래는 0,0인데 1,1로 시작했으니까 -1 씩 해주기

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(bfs(0,0))