def dfs(num):
  global answer
  if num == res:
    answer += 1
    return
  if num > res:
    return
  for i in range(1,4):
    dfs(num+i) 


T = int(input())
for t in range(T):
  answer = 0
  res = int(input())
  dfs(0)
  print(answer)