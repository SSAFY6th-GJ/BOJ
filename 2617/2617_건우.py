N , M = map(int, input().split())
check = [[[],[]] for _ in range(N+1)]
for _ in range(M):
  i, j = map(int, input().split())
  check[i][0].append(j)
  check[j][1].append(i)
  for k in check[j][0]:
    check[i][0].append(check[j][0][k])

  # for m in check[i][1]:
  #   check[j][1].append(check[i][1])
  

print(check)