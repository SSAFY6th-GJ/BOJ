from pprint import pprint
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
down_pos = 0

def expand():
    change = [[0]* C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                cnt = 0
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        change[ni][nj] += arr[i][j] // 5
                        cnt += 1
                arr[i][j] -= cnt * (arr[i][j] // 5)
    for i in range(R):
        for j in range(C):
            arr[i][j] += change[i][j]

def blow_up(i, j):
    if i > 0:
        i -= 1
    while i > 0:
        arr[i][j] = arr[i-1][j]
        i -= 1
    while j < C -1:
        arr[i][j] = arr[i][j+1]
        j += 1
    while i < up_pos[0]:
        arr[i][j] = arr[i+1][j]
        i += 1
    while j > 1:
        arr[i][j] = arr[i][j-1]
        j -= 1
    arr[i][j] = 0

def blow_down(i, j):
    if i < R-1 :
        i += 1
    while i < R-1 :
        arr[i][j] = arr[i+1][j]
        i += 1
    while j < C -1:
        arr[i][j] = arr[i][j+1]
        j += 1
    while i > down_pos[0]:
        arr[i][j] = arr[i-1][j]
        i -= 1
    while j > 1:
        arr[i][j] = arr[i][j-1]
        j -= 1
    arr[i][j] = 0
def get_pos():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                res = [i, j]
                return res 


up_pos = get_pos()
down_pos = [up_pos[0]+1, up_pos[1]]
for _ in range(T):
    expand()
    blow_up(up_pos[0], up_pos[1])
    blow_down(down_pos[0], down_pos[1])
answer = 0
for i in range(R):
    answer += sum(arr[i])

print(answer + 2)