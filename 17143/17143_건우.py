# from pprint import  pprint
# R, C, M = map(int, input().split())
# di = [-1, 1, 0, 0]
# dj = [0, 0, 1, -1]  #  위 아래 오른쪽 왼쪽

# arr = [[[]for _ in range(C)] for _ in range(R)]
# sha_list = []
# for _ in range(M):
#     # r,c 위치 s = 속력 d =방향  z = 크기
#     r, c, s, d, z = map(int, input().split())
#     arr[r-1][c-1].append([z, s, d])
#     sha_list.append([r,c,s,d,z])
# answer = 0
# print(sha_list)
# def moving():
#     global arr
#     tmp = [[0] * C for _ in range(R)]
#     n_sha_list = []
#     for sha in sha_list:
#         r, c, s, d, z = sha
#         if d == 0:
#             cycle = R * 2 -2
#             ns = s + R - j - 1
#             r = R -1
#             ns %= cycle
#             if ns < R:
#                 nr  -= s
#             if ns >= R:
#                 nr = s - R
#             if tmp[nr][c]:
#                 if tmp[nr][c][0] > z:
#                     pass
#                 else:
#                     tmp[nr][c] = [z, s, d]
#             else:
#                 tmp[nr][c] = [z, s, d]
#     arr = tmp
# for j in range(C):
#     for i in range(R):
#         if arr[i][j]:
#             answer += arr[i][j][0][0]
#             # print(arr[i][j][0])
#             arr[i][j] = []
#             break
#     moving()
#     pprint(arr)
# pprint(arr)



from pprint import  pprint
R, C, M = map(int, input().split())
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]  #  위 아래 오른쪽 왼쪽

arr = [[0]*C for _ in range(R)]
sha_list = []
for _ in range(M):
    # r,c 위치 s = 속력 d =방향  z = 크기
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = [z, s, d]
    sha_list.append([r-1,c-1,s,d,z])
answer = 0
# print(sha_list)
# pprint(arr)
def moving():
    global sha_list
    global arr
    tmp = [[0] * C for _ in range(R)]
    n_sha_list = []
    for sha in sha_list:
        r, c, s, d, z = sha
        if d == 1 or d == 2:
            cycle = R * 2 -2
            ns = s
            ns %= cycle
            while ns > 0:
                if d == 1:
                    ns -= 1
                    r -= 1
                elif d == 2:
                    ns -= 1
                    r += 1
                if r == 0:
                    d = 2
                elif r == R -1:
                    d = 1
            n_sha_list.append([r, c, s, d, z])
            tmp[r][c] = [z,s,d]
        if d == 3 or d == 4:
            cycle = C * 2 -2
            ns = s
            ns %= cycle
            while ns >0:
                if d == 3:
                    ns -= 1
                    c += 1
                elif d == 4:
                    ns -= 1
                    c -= 1
                if c == 0:
                    d = 3
                elif c == C -1:
                    d = 4
            n_sha_list.append([r, c, s, d, z])
            tmp[r][c] = [z,s,d]
    arr = tmp
    sha_list = n_sha_list
for j in range(C):
    for i in range(R):
        if arr[i][j]:
            answer += arr[i][j][0]
            arr[i][j] = 0
            for k in range(len(sha_list)):
                if sha_list[k][0] == i and sha_list[k][1] == j :
                    del sha_list[k]
                    break

            break

    moving()
    # pprint(arr)

print(answer)