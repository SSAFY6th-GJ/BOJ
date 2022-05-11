import sys
sys.stdin = open('점프점프.txt')

N = int(input())
lst = list(map(int, input().split()))
dp = [N] * (N)
dp[0] = 0
# 0 / 1-(1) / 2-min( (2, 3), 2) / 0 / 1-(3) / 3-min( (4,5,6), 4)
# 0     1           2             2     3          4
# dp = [0, 1, 2, 2, 3, 4, 4, 4, 5, 5]
for x in range(len(lst)):
    for y in range(1, lst[x]+1):
        if x + y < N:
            dp[x+y] = min(dp[x+y], dp[x]+1) # 새로운 곳 방문했을때
        else:
            break
print(dp)
if dp[N-1] != N:
    print(dp[N-1])
else:
    print(-1)
