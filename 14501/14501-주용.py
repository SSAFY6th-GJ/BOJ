import sys
sys.stdin = open('퇴사.txt')
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)
for i in range(N-1,-1,-1):
    if i + schedule[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(schedule[i][1] + dp[i+schedule[i][0]], dp[i+1])
print(dp[0])
