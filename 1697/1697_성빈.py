import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= arr and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

arr = 10 ** 5
visited = [0] * (arr+1)
n, k = map(int, input().split())

bfs()

'''
bfs로 풀었다.
4방향 대신 x-1, x+1, x*2 로 가고,
범위는 0 <= n <= 100,000
방문처리하면서 +1 처리
'''