from collections import deque
N = int(input())
lst = list(map(int,input().split()))
lst.sort()
budget = int(input())
lst = deque(lst)
answer = 0
# print(sum(lst))
if sum(lst) <= budget:
  answer = max(lst)
else:
  while True:
    sum_money = sum(lst)
    avg_money = budget // len(lst)
    if lst[0] < avg_money:
      budget -= lst[0]
      give_money = lst.popleft()
      answer =max(answer, give_money)
    else:
      give_money = budget// len(lst)
      answer = max(answer, give_money)
      break
print(answer)