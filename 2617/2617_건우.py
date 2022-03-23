N , M = map(int, input().split())
check = [[[],[]] for _ in range(N+1)]
for _ in range(M):
  i, j = map(int, input().split())
  check[i][1].append(j)
  check[j][0].append(i)

print(check)