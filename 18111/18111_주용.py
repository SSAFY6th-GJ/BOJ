

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(257):
    for x in range(M):
        for y in range(N):
            # 모르겠담