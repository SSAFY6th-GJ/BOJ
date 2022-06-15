from pprint import pprint
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
print(trees)
for _ in range(M):
    x,y,z = map(int,input().split())
    trees[x-1][y-1] = [z]

land = [[5]* N for _ in range(N)]
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
def year():
    # 봄여름
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if land[i][j] >= trees[i][j][k]:
                    if   trees[i][j][k] > 0:
                        
                        land[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                else:
                    land[i][j] += trees[i][j][k] // 2
                    trees[i][j][k] = -1
    print(land)
    # 가을
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] >0 and trees[i][j][k] % 5 == 0:
                    for d in range(8):
                        new_i = i + di[d]
                        new_j = j + dj[d]
                        if 0 <= new_i < N and 0 <= new_j < N:
                            trees[new_i][new_j].append(1)
                            trees[new_i][new_j].sort()
    # 겨울
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]
for _ in range(K):
    year()
    pprint(trees)
    pprint(land)
# print(trees)
answer = 0
for i in range(N):
    for j in range(N):
        for k in range(len(trees[i][j])):
            if trees[i][j][k] > 0:
                answer += 1
# print(trees)
print(answer)
