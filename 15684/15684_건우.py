N, M, H = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

def check():
    for i in range(1,N+1):
        r = i
        c = 0        
        while c < M :
            if arr[r][c] == 1:
                r -= 1
            elif arr[r-1][c] == 1:
                r += 1
            c += 1
        if arr[r][c] != i:
            return False
    return True

def dfs(r, c, k):

    else:
        
