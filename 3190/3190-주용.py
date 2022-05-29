import sys
sys.stdin = open('뱀.txt')
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
K = int(input())
base = [[0]* N for _ in range(N)]
snake = 1
# 오른쪽으로 출발
direction = 1
for _ in range(K):
    r, c = map(int, input().split())
    base[r-1][c-1] += 1     # 사과가 있는 곳을 + 1 해준다
L = int(input())
for _ in range(L):
    X, C = input().split()
while True:
