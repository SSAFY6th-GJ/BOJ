# import sys
# input = sys.stdin.readline
'''
+있는 곳을 괄호를 쳐야 최소값이 나옴
'''
numlist = input().split('-')
answer = []
for i in range(len(numlist)):
    sum = 0
    if '+' in numlist[i]:
        num = numlist[i].split('+')
        for j in num:
            sum += int(j)
        answer.append(sum)
    else:
        answer.append(int(numlist[i]))
result = answer[0]
for i in range(1, len(answer)):
    result -= answer[i]

print(result)