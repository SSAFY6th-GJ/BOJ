import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
answer = 999999
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            house.append([i, j])
        elif town[i][j] == 2:
            chicken.append([i, j])

for c in combinations(chicken, M):
    distance = 0
    for h in house:
        chicken_dis = 999999
        for i in range(M):
            chicken_dis = min(chicken_dis, abs(h[0] - c[i][0])+abs(h[1]-c[i][1]))
        distance += chicken_dis
    answer = min(answer, distance)

print(answer)

'''
m개 치킨집 선택했을 때 도시의 치킨거리 모두 구해보고 거기서 최소 값 출력
'''