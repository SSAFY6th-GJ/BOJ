import sys
sys.stdin = open('봄버맨.txt')
# 못품
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    global bomb

    while bomb:
        x,y = bomb.popleft()
        arr[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == 'O':
                arr[nx][ny] = '.'

R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
time = 0
bomb = deque()

for i in range(1, N+1):
    if i == 1:
        for x in range(R):
            for y in range(C):
                # 폭탄 있던 곳 저장
                if arr[x][y] == 'O':
                    bomb.append((x,y))
    elif i % 3 == 0:
        bfs()
        for x in range(R):
            for y in range(C):
                if arr[x][y] == 'O':
                    bomb.append((x,y))
    else:
        for x in range(R):
            for y in range(C):
                arr[x][y] = 'O'

print(arr)