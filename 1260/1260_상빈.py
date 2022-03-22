# from collections import deque
#
#
# def dfs(n):
#     v[n] = 1
#     lst.append(n)
#     for i in range(1, N+1):
#         if table[n][i] and not v[i]:
#             dfs(i)
#
# def bfs(n):
#     Q = deque()
#     v = [0] * (N + 1)
#     v[n] = 1
#     Q.append(n)
#     lst = []
#     while Q:
#         now = Q.popleft()
#         lst.append(now)
#         for i in range(1, N + 1):
#             if table[now][i] and not v[i]:
#                 Q.append(i)
#                 v[i] = 1
#
#     print(*lst)
#
#
# N, M, V = map(int, input().split())
# table = [[0]*(N+1) for _ in range(N+1)]
# for i in range(M):
#     n1, n2 = map(int, input().split())
#     table[n1][n2] = 1
#     table[n2][n1] = 1
#
# v = [0] * (N+1)
# lst = []
#
# dfs(V)
# print(*lst)
#
# bfs(V)


'''
    예전에 푼거
    
    이번에 새로 푼거
'''



from collections import deque


N, M, V = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    tree[s].append(e)                   # 방향성이 따로 없는 간선이므로 양쪽 다 추가하여 이어질 수 있도록 한다.
    tree[e].append(s)

v = [0] * (N+1)
v[V] = 1


def dfs(n):
    print(n, end=" ")
    for num in sorted(tree[n]):         # 같은 부모의 자식 노드일 경우 숫자가 작은 순서로 출력되야 하므로 정렬
        if not v[num]:
            v[num] = 1
            dfs(num)


dfs(V)
print()

v = [0] * (N+1)
v[V] = 1
Q = deque()
Q.append(V)
while Q:
    now = Q.popleft()
    print(now, end=" ")
    for num in sorted(tree[now]):       # 위와 같은 이유로 정렬
        if not v[num]:
            v[num] = 1
            Q.append(num)






































