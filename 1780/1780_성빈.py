import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
one = 0

def check(x,y,N):
    global minus, zero, one

    num = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != num:
                check(x, y, N//3)
                check(x, y+N//3, N//3)
                check(x, y+N//3*2, N//3)
                check(x+N//3, y, N//3)
                check(x+N//3, y+N//3, N//3)
                check(x+N//3, y+N//3*2, N//3)
                check(x+N//3*2, y, N//3)
                check(x+N//3*2, y+N//3, N//3)
                check(x+N//3*2, y+N//3*2, N//3)
                return

    if num == -1:
        minus += 1
    elif num == 0:
        zero += 1
    elif num == 1:
        one += 1

check(0,0,N)

print(minus)
print(zero)
print(one)

'''
0,0 부터 돌다가 숫자가 다른게 나오면 종이 9개로 자르고
0,0 / 0,3 / 0,6 
3,0 / 3,3 / 3,6
6,0 / 6,3 / 6,6
을 시작점으로 돌린다.
'''