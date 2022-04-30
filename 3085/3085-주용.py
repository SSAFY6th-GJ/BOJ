def check(arr):
    # 행 순회
    max_row = 0
    for i in range(N):
        row_cnt = 1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
        max_row = max(row_cnt, max_row)

    max_col = 0
    for i in range(N):
        col_cnt = 1
        for j in range(N-1):
            if arr[j][i] == arr[j+1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
        max_col = max(col_cnt, max_col)
    res = max(max_row, max_col)
    return res

N = int(input())
arr = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N-1):
        # 열 한번 바꾸고 최대개수 체크
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        col_tmp = check(arr)
        ans = max(col_tmp, ans)
        # 다시 돌려놓기
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
for i in range(N):
    for j in range(N-1):
        # # 행 한번 바꾸고 최대개수 체크
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
        row_tmp = check(arr)
        ans = max(row_tmp, ans)
        # 다시 돌려놓기
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
print(ans)
