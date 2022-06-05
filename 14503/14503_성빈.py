import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

clean =[[0] * M for _ in range(N)]
clean[r-1][c-1] = 1

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽



