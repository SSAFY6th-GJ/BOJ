question = input()
# 최소값으로 구하기 위해서는 - 빼고 다 괄호로 묶어서 계산 해야됨
question = question.split('-')
res = 0
# print(question)
for i in range(len(question)):
  tmp = question[i].split('+')
  sum_tmp = 0
  for j in tmp:
    sum_tmp += int(j)
    # 첫번째 인자값은 더해주고 나머지는 빼준다
  if i == 0:
    res += sum_tmp
  else:
    res -= sum_tmp
print(res)