import sys
input = sys.stdin.readline

N = int(input())
candy = [list(input()) for _ in range(N)]
answer = 0

def check(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
    return answer

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            temp = check(candy)
            if temp > answer:
                answer = temp

            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if i + 1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            temp = check(candy)
            if temp > answer:
                answer = temp
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(answer)

