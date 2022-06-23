r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]



def cal_R():
    global A
    tmp_A = []
    for i in range(len(A)):
        lst = []
        tmp = {}
        for k  in range(1, 101):
            tmp[k] = 0
        # print(tmp)
        for j in range(len(A[0])):
            if A[i][j] != 0:
               tmp[A[i][j]] += 1
        sorted_tmp = sorted(tmp.items(), key= lambda x: x[1])
        for n, m in sorted_tmp:
            if m != 0:
                lst.append(n)
                lst.append(m)
        tmp_A.append(lst)
    max_len = 0
    for i in range(len(A)):
        max_len = max(len(tmp_A[i]), max_len)
    for i in range(len(A)):
        if len(tmp_A[i]) < max_len:
            dif = max_len - len(tmp_A[i])
            add_zero = [0] * dif
            tmp_A[i].extend(add_zero)
    A = tmp_A
def cal_C():
    global A
    tmp_A = []
    for j in range(len(A[0])):
        lst = []
        tmp = {}
        for k  in range(1, 101):
            tmp[k] = 0
        # print(tmp)
        for i in range(len(A)):
            if A[i][j] != 0:
               tmp[A[i][j]] += 1
        sorted_tmp = sorted(tmp.items(), key= lambda x: x[1])
        for n, m in sorted_tmp:
            if m != 0:
                lst.append(n)
                lst.append(m)
        tmp_A.append(lst)
    max_len = 0
 
    for i in range(len(tmp_A)):
        max_len = max(len(tmp_A[i]), max_len)
    for i in range(len(tmp_A)):
        if len(tmp_A[i]) < max_len:
            dif = max_len - len(tmp_A[i])
            add_zero = [0] * dif
            tmp_A[i].extend(add_zero)
    tmp_arr = [[0] * len(tmp_A)  for _ in range(len(tmp_A[0]))]
    # print(tmp_A)
    # print(tmp_arr)

    for i in range(len(tmp_A)):
        for j in range(len(tmp_A[0])):
            tmp_arr[j][i] = tmp_A[i][j]
    A = tmp_arr



def answer(cnt):

    while cnt < 100:

        if len(A) >= len(A[0]):
            cal_R()
        else:
            cal_C()
        # print(A)
        if r>= len(A) and c >= len(A[0]):
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[r-1][c-1] == k:
                        return cnt
            cnt += 1
    return -1
if len(A) >= r and len(A[0]) >= c:
    if A[r-1][c-1] == k :
        print(0)
else:
    print(answer(1))