import pprint
N = int(input())

infos = [list(map(int, input().split())) for _ in range(N)]
arr = [[0] * 101 for _ in range(101)]

di = [0, -1, 0, 1]  # 우상좌하
dj = [1, 0, -1, 0]

def curve_list(d,g):
    curve = [d]
    for _ in range(g):
        for k in range(len(curve)-1, -1, -1):
            curve.append((curve[k] + 1) % 4)
    return curve




for info in infos:
    x, y, d, g = map(int, info)

    curves = curve_list(d,g)
    # print(curves)
    arr[y][x] = 1
    # print(curves)
    for curve in curves:
        y +=  di[curve]
        x +=  dj[curve]
        arr[y][x] = 1
    # pprint.pprint(arr)
answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1]==1:
            answer += 1


print(answer)
# pprint.pprint(arr)