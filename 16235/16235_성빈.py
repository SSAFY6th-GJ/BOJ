import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

# N*N, M 나무 정보, K년 후
N, M, K = map(int, input().split())

food_winter = [list(map(int, input().split())) for _ in range(N)] # 겨울에 뿌릴 양분

food = [[5] * N for _ in range(N)] # 현재 양분
# i행j열에 심어져 있는 나무 리스트 = k
tree = [[[] for _ in range(N)] for _ in range(N)] # 현재 나무

for _ in range(M):
    #x행y열 z살 나무 심음
    x,y,z = map(int, input().split())
    tree[x-1][y-1].append(z)

for _ in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            tree_dead = -1 # 죽은 나무 번호
            if tree[i][j]: # 나무가 있다면
                tree[i][j].sort() # 어린 나무 순으로 정렬
                for k in range(len(tree[i][j])): # 나무가 여러개 심어져있을수도
                    if food[i][j] >= tree[i][j][k]: # 그 땅의 양분이 그 나무 나이보다 많으면
                        food[i][j] -= tree[i][j][k] # 나무가 양분 먹고
                        tree[i][j][k] += 1 # 나이 1살 추가
                    else:
                        tree_dead = k # 양분 못먹는 나무 번호
                        break
                # 죽은 나무가 있다면
                if tree_dead != -1:
                    # 여름
                    # 죽은 나무 나이 2로 나눈 값이 그 땅의 양분이 됨
                    for k in range(tree_dead, len(tree[i][j])):
                        food[i][j] += tree[i][j][k] // 2

                    tree[i][j] = tree[i][j][:tree_dead]  # 죽은 나무보다 어린 나무들만 살아남음

    # 가을

    for i in range(N):
        for j in range(N):
            for t in tree[i][j]:
                # 나무나이가 5의 배수이면
                if t % 5 == 0:
                    for d in range(8):
                        ni = i + di[d]
                        nj = j + dj[d]
                        if 0 <= ni < N and 0 <= nj < N:
                            # 1살 나무 번식함
                            tree[ni][nj].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            food[i][j] += food_winter[i][j] # 땅에 양분 추가

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j]) # k년 후 남은 나무 개수

print(answer)


