import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [0, stairs[0]]
if n > 1:
    dp.append(stairs[0] + stairs[1])
for i in range(3, n+1):
    dp.append(max(dp[i-2]+stairs[i-1], dp[i-3]+stairs[i-1]+stairs[i-2]))
print(dp[n])
'''
계단 1개 2개 있을때는 1,2개 모두 올라가는게 최대값
3개부터 dp 돌려준다.
계단 3개 연속으로 올라갈 수 없다.
ㅁ + X + ㅇ + ㅇ
     ㅁ + X + ㅇ
'''