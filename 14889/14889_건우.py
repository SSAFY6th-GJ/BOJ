from copy import deepcopy
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start = []
link = []
# 12 13 14
# 23 24
# 34 


def dfs(L, S):
    if L == N//2:
        start.append(deepcopy(res))
    else:
        for i in range(S, N):
            res[L] = i
            dfs(L + 1, i + 1)
            
res = [0] * (N//2)
dfs(0,0)
# print(start)
answer = 40000
for lst in start:
    start_sum = 0
    link_sum = 0
    for i in range(N):
        for j in range(N):
            if i in lst and j in lst:
                start_sum += arr[i][j]
            elif i not in lst and j not in lst:
                link_sum += arr[i][j]
    answer = min(abs(start_sum-link_sum),answer)
print(answer)