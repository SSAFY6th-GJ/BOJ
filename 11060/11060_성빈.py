import sys
input = sys.stdin.readline

N = int(input())
maze = list(map(int, input().split()))

dp = [N+1]*N
dp[0] = 0

for i in range(N):
    for j in range(1, maze[i]+1):
        if i+j < N:
            dp[i+j] = min(dp[i]+1, dp[i+j])

if dp[N-1] == N+1:
    print(-1)
else:
    print(dp[N-1])


'''
maze = [1, 2, 0, 1, 3, 2, 1, 5, 4, 2]


dp = [0, 11, 11, 11, 11, 11, 11, 11, 11, 11]
dp = [0, 1, 2, 2, 3, 4, 4, 4, 5, 5]

설명을 읽어봐도 이해가 안갑니다링 .........;;;
'''