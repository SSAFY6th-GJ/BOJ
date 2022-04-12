import sys
input = sys.stdin.readline

n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))

dp = [0, grape[0]]
if n > 1:
    dp.append(grape[0] + grape[1])

for i in range(3, n+1):
    dp.append(max(dp[i-2]+grape[i-1], dp[i-1], dp[i-3]+grape[i-1]+grape[i-2]))

print(dp[n])

'''
1,2잔만 있을때는 1,2잔 모두 마시는게 최대값
3잔부터 dp 돌려준다.
포도주 3잔을 연속으로 마실 수 없다.
ㅁ + X + ㅇ + ㅇ
     ㅁ + X + ㅇ
         ㅁ + X
'''