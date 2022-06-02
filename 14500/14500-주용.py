import sys
sys.stdin = open('테트로미노.txt')

def dfs()
    pass

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

# 어렵네..