import sys
input = sys.stdin.readline

n = int(input())
dp = [k for k in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
        # 제곱수로 표현할 때 가장 항의 개수가 작은 j를 찾는다
        # dp[7] = dp[7 - 2*2] + 1
print(dp[n])
'''
초기 dp에 저장되는 배열은 0~n까지이며
이중 for문을 돌면서 제곱수가 현재의 수보다 크다면 넘기고
현재의 수보다 제곱수가 작다면, 현재의 수 - 제곱수를 하여 그 값에 대한 dp값을 가져온다.
이때 제곱수를 빼고 난 값의 dp값을 가져왔으므로, +1을 해주어 빼준 제곱수(j)의 경우를 더해준다.

[0,1,2,3,4,5,6,7]
[0,1,2,3,1,2,3,4]
'''


# cnt = 0
#
# while n >= 0:
#     if n == 1:
#         cnt += 1
#         break
#     for i in range(n//2, 0, -1):
#         if i*i <= n:
#             n -= i**2
#             cnt += 1
#             # print(i)
#             break
# print(cnt)

# while n > 0:
#     for i in range(1, 101):
#         if i*i > n:
#             n -= (i-1)**2
#             cnt += 1
#             break
#
# print(cnt)

# while n > 0:
#     for i in range(100, 0, -1):
#         if i*i <= n:
#             n -= (i-1)**2
#             cnt += 1
#             break
# print(cnt)



