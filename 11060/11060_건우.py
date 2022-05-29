N = int(input())
arr = list(map(int, input().split()))
arr_check = [1001] * N
arr_check[0] = 0
for i in range(len(arr)):
  jump_can = arr[i]
  for jump in range(1, jump_can + 1):
      if i + jump < N:
        arr_check[i+jump] = min(arr_check[i] + 1, arr_check[i+jump])
print(arr_check[N-1])