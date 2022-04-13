sys.stdin = open('계단오르기.txt')

N = int(input())
step = [int(input()) for _ in range(N)]

dp = [0] * 301
#밑에 if 조건 안하니까 인덱스에러난다. 계단의 수가 1개랑 2개 있을때도 고려해줘야한다.
if N == 1:
    dp[0] = step[0]
elif N == 2:
    dp[0] = step[0]
    dp[1] = max(step[0] + step[1], step[1], dp[0])
elif N >= 3:
    dp[0] = step[0]
    dp[1] = max(step[0] + step[1], step[1], dp[0])
    dp[2] = max(step[0] + step[2], step[1] + step[2], step[2])
    for i in range(3, N):
        dp[i] = max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])

print(dp[N-1])