


from copy import copy, deepcopy


N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cameras = []

answer = 1000000
for i in range(N):
    for j in range(M):
        if room[i][j] in [1, 2, 3, 4, 5]:
            cameras.append((i,j,room[i][j]))




def right(temp, i, j):

    while j < M-1:
        j += 1
        if temp[i][j] == 0:
            temp[i][j] = '#'
        elif temp[i][j] == 6:
            return


def left(temp, i, j):

    while j > 0:
        j -= 1
        if temp[i][j] == 0:
            temp[i][j] = '#'
        elif temp[i][j] == 6:
            return

def down(temp, i, j):

    while i < N-1:
        i += 1
        if temp[i][j] == 0:
            temp[i][j] = '#'
        elif temp[i][j] == 6:
            return

def up(temp, i, j):

    while i > 0:
        i -= 1
        if temp[i][j] == 0:
            temp[i][j] = '#'
        elif temp[i][j] == 6:
            return
def back(temp):
    for i in range(N):
        for j in range(M):
            if room[i][j] != temp[i][j]:
                room[i][j] = 0


def dfs(room, num):
    global answer
    
    for n in range(num, len(cameras)):
        i,j = cameras[n][0], cameras[n][1]
        camera = room[i][j]

            # 1번 카메라 일때
        if camera == 1:
            temp = deepcopy(room)
            right(temp, i, j)
            dfs(temp, num+1)
            
            # room[i][j] = 1
            temp = deepcopy(room)
            left(temp, i,j)
            dfs(temp, num+1)

            # room[i][j] = 1
            temp = deepcopy(room)
            up(temp, i,j)
            dfs(temp ,num+1)
            # back(temp)
            # room[i][j] = 1
            temp = deepcopy(room)
            down(temp, i, j)
            dfs(temp, num+1)
            # back(temp)
            # room[i][j] = 1
        # 2번 카메라 일때
        if camera == 2:

            right(temp,i,j)
            left(temp,i,j)
            dfs(temp, num+1)
            # back(temp)
            # room[i][j] = 2
            up(temp,i,j)
            down(temp,i,j)
            dfs(temp, num+1)
            # back(temp)
            # room[i][j] = 2
        # 3번 카메라 일때

        if camera == 3:

            right(temp,i,j)
            up(temp,i,j)
            dfs(temp, num+1)
            # back(temp)
            # room[i][j] = 3
            right(temp, i,j)
            down(temp, i,j)
            dfs(temp, num+1)
            # back(temp)
            # room[i][j] = 3
            down(i,j)
            left(i,j)
            dfs(num+1)
            back(temp)
            room[i][j] = 3
            left(i,j)
            up(i,j)
            dfs(num+1)
            back(temp)
            room[i][j] = 3
        # 4번 카메라 일때

        if camera == 4:

            left(i,j)
            up(i,j)
            right(i,j)
            dfs(num+1)
            back(temp)
            room[i][j] = 4
            up(i,j)
            right(i,j)
            down(i,j)
            dfs(num+1)
            back(temp)
            room[i][j] = 4
            right(i,j)
            down(i,j)
            left(i,j)
            dfs(num+1)
            back(temp)
            room[i][j] = 4
            down(i,j)
            left(i,j)
            up(i,j)
            dfs(num+1)
            back(temp)
            room[i][j] = 4
        # 5번 카메라 일때
        if camera == 5:

            left(i,j)
            up(i,j)
            right(i,j)
            down(i,j)
            dfs(num+1)
            back(temp)
            room[i][j] = 5
    res = 0
    for i in range(N):
        res += room[i].count(0)
    answer = min(res, answer)
dfs(room, 0)
# print(cameras)
print(answer)