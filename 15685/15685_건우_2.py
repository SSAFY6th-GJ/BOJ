import pprint
N = int(input())

infos = [list(map(int, input().split())) for _ in range(N)]
arr = [[0] * 10 for _ in range(10)]

di = [0, -1, 0, 1]  # 우상좌하
dj = [1, 0, -1, 0]

def curve_list(d,g):
    curve = [d]
    for _ in range(g):
        for k in range(len(curve)-1, -1, -1):
            curve.append((curve[k] + 1) % 4)
    return curve

def drangon_curve(curves,x, y):
    arr[x][y] = 1
    
    for curve in curves:
        x +=  di[curve]
        y +=  dj[curve]
        arr[x][y] = 1


for info in infos:
    x, y, d, g = map(int, info)

    curves = curve_list(d,g)
    drangon_curve(curves, x, y)
pprint.pprint(arr)