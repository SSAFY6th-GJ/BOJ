from sys import stdin

N, M , B = map(int,input().split())
arr = []

# 땅의 높이를 몇으로 할건지 먼저 정한다
# 제일 빨리 하기 위해선 땅의 평균 높이로 맞춘다
# sum_ddang = 0
# for i in range(N):
#   for j in range(M):
#     sum_ddang += arr[i][j]
# avg_ddang = math.ceil(sum_ddang / (N*M))
# total_blocks = sum_ddang + B
# if total_blocks // (N*M) < avg_ddang:
#   avg_ddang -= 1

def check_time(max_height):
  global total_time
  global answer
  global answer_height
  for i in range(N):
    for j in range(M):
      if arr[i][j] > max_height:
        total_time += (arr[i][j] -max_height) * 2
      else:
        total_time +=  max_height - arr[i][j]
      if total_time > answer:
        return
  answer = total_time
  answer_height = max_height

max_height = 0
sum_blocks = 0
answer = 100000000000000000
answer_height = 0
total_time = 0

for i in range(N):
  lst = list(map(int,stdin.readline().split()))
  arr.append(lst)
  sum_blocks += sum(lst)
  if max(lst) > max_height:
    max_height = max(lst)
# avg_blocks = round(sum_blocks / (N*M))
sum_blocks += B
# if avg_blocks > sum_blocks // (N*M):
#   avg_blocks -= 1
# check_time(avg_blocks)


# print(sum_blocks)
while max_height >= 0:
  total_time = 0
  if max_height > sum_blocks //(N*M):
    max_height -= 1
  else:
    check_time(max_height)
    max_height -= 1


print(answer, answer_height)