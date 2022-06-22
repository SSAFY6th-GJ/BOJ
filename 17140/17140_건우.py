r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]



def cal_R():
    global A
    tmp_A = []
    for i in range(len(A)):
        lst = []
        tmp = {}
        for k  in range(1, len(A[0]) + 1):
            tmp[k] = 0
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
        for k  in range(1, len(A) + 1):
            tmp[k] = 0
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
    for i in range(len(A)):
        max_len = max(len(tmp_A[i]), max_len)
    for i in range(len(A)):
        if len(tmp_A[i]) < max_len:
            dif = max_len - len(tmp_A[i])
            add_zero = [0] * dif
            tmp_A[i].extend(add_zero)
    tmp_arr = [[0] * len(tmp_A)  for _ in range(len(tmp_A[0]))]
    print(tmp_A)
    for i in range(len(tmp_A)):
        for j in range(len(tmp_A[0])):
            tmp_arr[i][j] = tmp_A[i][len(tmp_A[0])-1-i]
    A = tmp_A
    print(tmp_arr)


def after1sec():
    if len(A) >= len(A[0]):
        cal_C()
        print('c')
    else:
        cal_R()
        print('R')

after1sec()
