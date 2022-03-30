T = int(input())
for tc in range(1, T+1):
  N = int(input())
  woods = list(map(int, input().split()))
  woods.sort()
  res = []
  res.append(woods[0])
  res.append(woods[1])
  for i in range(2, len(woods)):
    if woods[i] - res[0] > woods[i] - res[-1]:
      res.insert(0, woods[i])
    else:
      res.append(woods[i])
  answer = 0

  for j in range(len(res)):
    if abs(res[j] - res[j-1]) > answer:
      answer = abs(res[j] - res[j-1])

  print(answer)