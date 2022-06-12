N, L = map(int, input().split())
Arr = [list(map(int, input().split())) for _ in range(N)]

def is_path(i):
    for j in range(N-1):
        if Arr[i][j] != Arr[i][j+1]:
            #차이가 1일때만 다리를 놓을수 있다.
            if abs(Arr[i][j] - Arr[i][j+1]) == 1:
                #왼쪽 숫자가 작으면 왼쪽 에 L개의 블록 만큼 숫자가 같아야한다
                if Arr[i][j] < Arr[i][j+1]:
                    if 0 <= j - (L -1):
                        for k in range(L):
                            if visited[j-k] != 0:
                                return False
                            else:
                                visited[j-k] = 1
                            if Arr[i][j-k] != Arr[i][j]:
                                return False
                    else:
                        return False
                #오른쪽 숫자가 작으면 오른쪽 L개의 블록만큼 숫자가 같아야한다.
                else:
                    if j + L < N:
                        for k in range(L):
                            if visited[j+k+1] != 0:
                                return False
                            else:
                                visited[j+k+1] = 1
                            if Arr[i][j+k+1] != Arr[i][j+1]:
                                return False
                    else:
                        return False

            else:
                return False
    return True
answer = 0
for i in range(N):
    visited = [0] * N
    if is_path(i):
        answer += 1
rotate_Arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        rotate_Arr[j][N-1-i] = Arr[i][j]
Arr = rotate_Arr
for i in range(N):
    visited = [0] * N
    if is_path(i):
        answer += 1
print(answer)
