from itertools import combinations
from copy import deepcopy
from collections import deque
from pprint import pprint
N, M = map(int, input().split())
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
arr = [list(map(int, input().split())) for _ in range(N)]

virus_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2: 
            virus_list.append([i,j])
            arr[i][j] == '*'
        elif arr[i][j] == 1:
            arr[i][j] = '-'
        elif arr[i][j] == 0:
            arr[i][j] = '%'
    
virus_combi = list(combinations(virus_list, M))

def bfs(active_virus):
    que = deque(active_virus)
    while que:
        i, j = que.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and tmp[ni][nj] == '%':

                tmp[ni][nj] = tmp[i][j] + 1
                que.append([ni,nj])


def get_res():
    res_time = 0
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == '%':
                return 99999
            elif tmp[i][j] != '-' and tmp[i][j] != '*' :
                res_time = max(res_time, tmp[i][j])
    return res_time


answer = 1000000
is_possible = 0
for active_virus in virus_combi:

    res = 0
    no_active = []
    for virus in virus_list:
        if virus not in active_virus:
            no_active.append(virus) 
    tmp = deepcopy(arr)
    # pprint(tmp)
    for n in range(M):
        i,j = active_virus[n]
        tmp[i][j] = 0
    for m in range(len(no_active)):
        i, j = no_active[m]
        tmp[i][j] = '*'
    bfs(active_virus)
    res = get_res()
    if res == 99999:
        is_possible += 1
    

    answer = min(res, answer)
if is_possible == len(virus_combi):
    answer = -1

print(answer)