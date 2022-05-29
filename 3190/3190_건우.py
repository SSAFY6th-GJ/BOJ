
N = int(input())
maps = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
  i, j = map(int, input().split())
  maps[i][j] = 2
L = int(input())
direcs = [list(input().split()) for _ in range(L)]

print(direcs)


print(maps)