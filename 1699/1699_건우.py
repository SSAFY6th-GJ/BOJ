# import sys
# sys.setrecursionlimit(10**6)
import math

N = int(input())
answer = 100000
def solve(K, cnt):
  global answer
  if cnt >= answer:
    return
  if K == N:
    answer = min(cnt, answer)
    return
  for i in range(math.floor(math.sqrt(N)),0,-1):
    if i ** 2 + K > N:
      return
    solve(K + i ** 2, cnt + 1)
solve(0,0)
print(answer)