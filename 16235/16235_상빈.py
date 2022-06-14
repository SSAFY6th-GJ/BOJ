def spring():
    land = [[[] for _ in range(N+1)] for _ in range(N)]
    for g in trees:
        for tree in trees[g]:
            land[tree[1]][tree[2]].append(tree)

    for i in range(N):
        for j in range(N):
            if land[i][j]:
                land[i][j].sort()
                for tree in land[i][j]:
                    if farm[i][j] >= tree[0]:
                        farm[i][j] -= tree[0]
                        tree[0] += 1
                    else:
                        tree[3] = 0


def summer():
    for tree in trees:
        if not tree[3]:
            farm[tree[1]][tree[2]] += tree[0]//2
            trees.remove(tree)


def fall():
    for tree in trees:
        if not tree[0] % 5:

            y = tree[1]
            x = tree[2]

            for i in range(8):

                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < N and 0 <= nx < N:
                    trees.append([1, ny, nx, 1])


def winter():
    for i in range(N):
        for j in range(N):
            farm[i][j] += feed[i][j]


N, M, K = map(int, input().split())

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

farm = [[5]*N for _ in range(N)]

feed = [list(map(int, input().split())) for _ in range(N)]

trees = {}

for _ in range(M):
    x, y, z = map(int, input().split())
    if z in trees.keys():
        trees[z].append([y - 1, x - 1, 1])
    else:
        trees[z] = [y - 1, x - 1, 1]

for i in range(K):
    spring()
    summer()
    fall()
    winter()

ans = 0

for tree in trees:
    if tree[3]:
        ans += 1

print(ans)