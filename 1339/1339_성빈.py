import sys
input = sys.stdin.readline

alpha = {}

n = int(input())
lst = []
for i in range(n):
    a = list(input().rstrip())
    lst.append(a)

# print(lst)
for i in range(n):
    for j in range(len(lst[i])-1, -1, -1): # 2,1,0
        key = lst[i][j]
        k = len(lst[i])-1 - j
        if key not in alpha:
            alpha[key] = 10**(len(lst[i])- k)
        else:
            alpha[key] += 10**(len(lst[i])-k)

print(alpha)

'''
자릿수만큼 넣어서 
큰 자리수부터 9,8,7,6 .. 곱해주려했는데 딕셔너리 못 구하겠삼
'''