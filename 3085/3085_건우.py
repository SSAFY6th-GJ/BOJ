# N = int(input())
# arr = [list(map(str, input())) for _ in range(N)]
# res = 0
# def check_max():
#   max_cnt = 0
#   for i in range(N):
#     cnt = 0
#     pre_color = ''
#     for j in range(N):
#       if j == 0:
#         cnt += 1
#         pre_color = arr[i][j]
#       elif pre_color == arr[i][j]:
#         cnt += 1
#       else:      
#         cnt = 1
#       pre_color = arr[i][j]
#       max_cnt = max(max_cnt,cnt)
#   for j in range(N):
#     cnt = 0
#     pre_color = ''
#     for i in range(N):
#       if i == 0:
#         cnt += 1
#         pre_color = arr[i][j]
#       elif pre_color == arr[i][j]:
#         cnt += 1
#       else:      
#         cnt = 1
#       pre_color = arr[i][j]
#       max_cnt = max(max_cnt,cnt)
#   return max_cnt

# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
# for i in range(N):
#   for j in range(N):
#     for d in range(4):
#       new_i = i + di[d]
#       new_j = j + dj[d]
#       if 0<= new_i < N and 0<= new_j < N and arr[i][j] != arr[new_i][new_j]:
#         arr[i][j], arr[new_i][new_j] = arr[new_i][new_j], arr[i][j]
#         res = max(res,check_max())
#         arr[i][j], arr[new_i][new_j] = arr[new_i][new_j], arr[i][j]
        
# print(res)



N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
res = 0
def check_max():
  max_cnt = 0
  for i in range(N):
    cnt = 0
    pre_color = ''
    for j in range(N):
      if j == 0:
        cnt += 1
        pre_color = arr[i][j]
      elif pre_color == arr[i][j]:
        cnt += 1
      else:      
        cnt = 1
      pre_color = arr[i][j]
      max_cnt = max(max_cnt,cnt)
  for j in range(N):
    cnt = 0
    pre_color = ''
    for i in range(N):
      if i == 0:
        cnt += 1
        pre_color = arr[i][j]
      elif pre_color == arr[i][j]:
        cnt += 1
      else:      
        cnt = 1
      pre_color = arr[i][j]
      max_cnt = max(max_cnt,cnt)
  return max_cnt

di = [1, 0]
dj = [0, 1]
for i in range(N):
  for j in range(N):
    for d in range(2):
      new_i = i + di[d]
      new_j = j + dj[d]
      if 0<=new_i<N and 0<= new_j < N  and arr[i][j] != arr[new_i][new_j]:
        arr[i][j], arr[new_i][new_j] = arr[new_i][new_j], arr[i][j]
        res = max(res,check_max())
        arr[i][j], arr[new_i][new_j] = arr[new_i][new_j], arr[i][j]
        
print(res)