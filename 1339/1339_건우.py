# N = int(input())
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# cnt = {}
# res = {}
# lst = [[] for _ in range(9)]
# for _ in range(N):
#   num = input()
#   for i in range(len(num)):
#     lst[len(num)-i].append(num[i])
#     if num[i] in cnt:
#       cnt[num[i]] += 1
#     else:
#       cnt[num[i]] = 1
#       res[num[i]] = 0
# print(lst)
# print(cnt)
# for j in range(8,0,-1):
#   if len(lst[j]) == 1:
#     res[num[lst[j][0]]] = numbers.pop()
#   elif len(lst[j]) > 1:


answer = 0
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = {}
N = int(input())
for _ in range(N):
  num = input()
  for i in range(len(num)):
    if num[i] in cnt:
      cnt[num[i]] += 10**(len(num)-i-1)
    else:
      cnt[num[i]] = 10**(len(num)-i-1)
sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
print(sorted_cnt)
for k in sorted_cnt:
  answer += numbers.pop() * k[1]
print(answer)