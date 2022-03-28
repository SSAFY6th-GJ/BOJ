dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c, num):
    # if len(num) == 6 and num not in res: # 이거랑

    # if len(num) == 6:
    #     if num not in res:        # 이거랑의 차이점 똑같은 의미미

   #         res.append(num)
#         return    # return 뒤에 없을때는 무슨 의미?? 그 조건일때 끝낸다.(끝날 타이밍)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, num + arr[nr][nc])

arr = [list(map(str, input().split())) for _ in range(5)]
res = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(res))