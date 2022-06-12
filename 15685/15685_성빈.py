import sys
input = sys.stdin.readline

N = int(input())

# 0우 1상 2좌 3하
dx = [1,0,-1,0]
dy = [0,-1,0,1]

arr = [[0]*101 for _ in range(101)] # 100 * 100

for i in range(N):

    x, y, d, g = map(int, input().split())
    arr[x][y] = 1

    move = [d]
    # 세대만큼 반복

    for j in range(g):
        arr_g = []
        for k in range(len(move)):
            arr_g.append((move[-k-1] +1) % 4)

        move.extend(arr_g)
        '''
        append, extend 차이점
        둘 다 리스트에 추가하는 문법
        append.([1,2]) = [[1,2]]
        extend([1,2]) = [1,2]
        '''

    # arr에 드래곤커브 좌표 찍어주기
    for d in move:
        nx = x + dx[d]
        ny = y + dy[d]
        arr[nx][ny] = 1
        x, y = nx, ny

answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            answer += 1

print(answer)