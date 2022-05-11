# import sys
# input = sys.stdin.readline

def step1(arr):
    for x in range(R):
        for y in range(C):
            if arr[x][y] == 'O':
                arr[x][y] = 2

            elif arr[x][y] == 2:
                arr[x][y] = 1
            elif arr[x][y] == '.':
                arr[x][y] = 'O'
            elif arr[x][y] == 1:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        arr[nx][ny] = '.'

def step2(arr):
    for x in range(R):
        for y in range(C):
            if arr[x][y] == '.':
                arr[x][y] = 'O'
            elif arr[x][y] == 2:
                arr[x][y] = 1

            elif arr[x][y] == 1:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        arr[nx][ny] = '.'
            elif arr[x][y] == 'O':
                arr[x][y] = 2

def step3(arr):
    for x in range(R):
        for y in range(C):
            if arr[x][y] == 1:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        arr[nx][ny] = '.'
            elif arr[x][y] == 'O':
                arr[x][y] = 2

            elif arr[x][y] == '.':
                arr[x][y] = 'O'
            elif arr[x][y] == 2:
                arr[x][y] = 1

R, C, N = map(int, input().split())
map = [list(input()) for _ in range(R)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

time = N-1
while time:
    step1(map)
    step2(map)
    time -= 1
    if time == 0:
        break
    step3(map)
    time -= 1

# for i in range(R):
#     for j in range(C):
#         if map[i][j] == 1:
#             map[i][j] = 'O'
#         elif map[i][j] == 2:
#             map[i][j] = 'O'

for i in range(R):
    # print(''.join(map[i]))
    print(map[i])
