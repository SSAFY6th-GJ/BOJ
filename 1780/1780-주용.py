import sys
sys.stdin = open('종이의 개수.txt')
sys.setrecursionlimit(10**9)
def check(i, j, N):
    global num_minus_one, num_one, num_zero
    num = arr[i][j]
    for x in range(i, i+N):
        for y in range(j, j+N):
            if num != arr[x][y]:
                tmp_N = N//3
                for r in range(0, 3):
                    for c in range(0, 3):
                        check(i + r * tmp_N, j + c * tmp_N, tmp_N)
                return      # return 안쓰면 엉뚱한 답 나온다
    if num == -1:
        num_minus_one += 1
    elif num == 1:
        num_one += 1
    else:
        num_zero += 1

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
num_minus_one = 0
num_zero = 0
num_one = 0
check(0, 0, N)
print(num_minus_one)
print(num_zero)
print(num_one)