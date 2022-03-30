N = int(input())
res = []
answer = 0
res_list = [list(map(int, input().split())) for _ in range(N)]

res_list.sort(key=lambda x:(x[1],x[0]))
finish_time = 0
for i in range(len(res_list)):
  if res_list[i][0] >= finish_time:
    answer += 1
    finish_time = res_list[i][1]

print(answer)


# lambda로 정리할 때 x: x[1] 로만 하면 왜 틀리게 나오지 ?