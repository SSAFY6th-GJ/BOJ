import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
answer = 10000000
cnt = 0
def solve(N, K, cnt):
  global answer
  if cnt >= answer:
    return
  if N == K:
    answer = min(answer,cnt)
    return
  elif N < K:
    if K % 2 == 0 and N - K//2 < N - K :
      solve(N, K//2, cnt+1)
    solve(N, K-1, cnt+1)
    solve(N, K+1, cnt+1)
  elif N > K:
    solve(N, K+1, cnt+1)

solve(N,K,cnt)
print(answer)