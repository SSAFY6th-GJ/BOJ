N = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 해당 자리 주위에 좋아하는 학생이 얼마나 있는지 확인하는 함수
def aroundlike(y, x, n):
    cnt = 0
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < N and 0 <= xx < N and table[yy][xx] in students[n][1:]:
            cnt += 1

    return cnt


# 스텝1 : 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
def step1(n):

    newlst = []
    maxlike = 0

    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                nowlike = aroundlike(i, j, n)
                if nowlike > maxlike:
                    maxlike = nowlike
                    newlst = [[i, j]]
                elif nowlike == maxlike:
                    newlst.append([i, j])

    return newlst


# 해당 자리 주위에 비어있는 자리가 얼마나 있는지 확인하는 함수
def aroundempty(y, x):

    cnt = 0

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < N and 0 <= xx < N and table[yy][xx] == 0:
            cnt += 1

    return cnt


# 스텝2 : 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
def step2(lst):

    newlst = []
    maxempty = 0

    for chair in lst:
        y = chair[0]
        x = chair[1]

        nowempty = aroundempty(y, x)

        if nowempty > maxempty:
            maxempty = nowempty
            newlst = [[y, x]]
        elif nowempty == maxempty:
            newlst.append([y, x])

    return newlst


# 스텝3 : 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
def step3(lst):
    for i in range(N):
        for j in range(N):
            if [i, j] in lst:
                return i, j


# 학생의 자리 만족도를 구하는 함수
def calc(y, x):

    now = table[y][x]
    cnt = 0
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < N and 0 <= xx < N and table[yy][xx] in students[now-1][1:]:
            cnt += 1

    if not cnt:
        return 0
    else:
        return 10**(cnt-1)


students = [list(map(int, input().split())) for _ in range(N**2)]

table = [[0]*N for _ in range(N)]
'''
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
'''
for i in range(N**2):
    step1_list = step1(i)
    if len(step1_list) == 1:
        table[step1_list[0][0]][step1_list[0][1]] = students[i][0]
    else:
        step2_list = step2(step1_list)
        if len(step2_list) == 1:
            table[step2_list[0][0]][step2_list[0][1]] = students[i][0]
        else:
            y, x = step3(step2_list)
            table[y][x] = students[i][0]

students.sort()

happy = 0
for i in range(N):
    for j in range(N):
        happy += calc(i, j)

print(happy)