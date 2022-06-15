from math import sqrt
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken_lst = []
home_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            # arr[i][j] = 0
            chicken_lst.append((i,j))
        elif arr[i][j] == 1:
            home_lst.append((i,j))
answer = 1000000

def get_distance(lst):
    global answer
    dist = 0
    for home in home_lst:
        home_i, home_j = home[0], home[1]  
        tmp =  10000                  
        for chicken in lst:
            chicken_i, chicken_j = chicken[0], chicken[1]
            tmp = min(tmp, abs(chicken_i-home_i) + abs(chicken_j-home_j))
        dist += tmp

    answer = min(answer, dist)




    


def dfs(s, lst):
    if len(lst) == M:
        # print(lst)
        get_distance(lst)
        return

    for i in range(s, len(chicken_lst)):
        lst.append(chicken_lst[i])
        dfs(i+1, lst)
        lst.pop()

dfs(0,[])

print(answer)