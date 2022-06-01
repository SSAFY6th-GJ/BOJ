import sys
sys.stdin = open('로봇청소기.txt')

N, M = map(int, input().split())    # 세로 N, 가로 M
r, c, d = map(int, input().split()) # 현재있는 좌표 r,c와 방향 d
arr = [list(map(int, input().split())) for _ in range(N)]
# 빈칸은 0 벽은 1
# d 0 북, 1 동, 2 남, 3 서
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0
while True:
    if arr[r][c] == 0:
        arr[r][c] = 2   # 0이면 2로 만들기(청소)
        cnt += 1        # 청소한 칸 갯수 세기
    # 북0->서3, 동1->북0, 남2->동1, 서3->남2
    nr = r + dr[(d+3)%4]
    nc = c + dc[(d+3)%4]
    # 2-a
    if arr[nr][nc] == 0:    # 왼쪽이 청소가 안되어있으면
        d = (d+3)  % 4  # 회전하기
        r, c = nr, nc   # 이동(한칸 전진)
        continue
    # 2-b
    if arr[r-1][c] and arr[r][c-1] and arr[r+1][c] and arr[r][c+1]: # 4번 연속 실행
        nr = r + dr[(d+2)%4] # 뒤 위치 탐색
        nc = c + dc[(d+2)%4] # 뒤 위치 탐색
        if arr[nr][nc] == 1:    # 벽이면 멈추기
            break
        else:
            r, c = nr, nc
            continue
    if arr[nr][nc]: # 청소했으면
        d = (d+3) % 4   # 회전
        continue
print(cnt)