import sys

sys.stdin = open('구슬찾기.txt')


## 아 너무너무 너무너무 모르겠습니다...# dfs로 어떻게 푸는건지.. 휴...
def dfs():


N, M = map(int, input().split())
base = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())  # x 가 y보다 무겁다
    base[x].append(y)
    base[y].append(x)
print(base)
#  4 > 3  5 > 1      4 > 2 > 1