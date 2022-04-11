import sys
sys.setrecursionlimit(10**6)

N = int(input())
table = []
for _ in range(N):
  a = int(input())
  table.append(a)
visited = [0] * N
sum_value = [0] * N
answer= 0
def solve(res,index):
  if sum_value[index] == 0:
    sum_value[index] = res
  if sum_value[index] > res:
    return
  global answer
  if index == N - 1:
    if res > answer:
      answer = res
    return

  if index > 1:
    if visited[index-1] == 1 and visited[index-2] == 1:
      solve(res,index + 1)
      return
    else:
      visited[index] = 1
      solve(res+table[index], index+1)
      visited[index] = 0
      solve(res, index + 1)
  else:
    visited[index] = 1
    solve(res+table[index], index+1)
    visited[index] = 0
    solve(res, index + 1)
solve(0,0)
print(answer)