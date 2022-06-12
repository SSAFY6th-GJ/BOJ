import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

players = [p for p in range(N)]
team = []

# 가능한 팀 모두 뽑은 거
for i in list(combinations(players, N//2)):
    team.append(i)

mingap = 9999999
for i in range(len(team)//2):
    # a팀
    Ateam = 0 #a팀 능력치
    for j in range(N//2):
        player = team[i][j]
        for k in team[i]:
            Ateam += S[player][k]

    # b팀
    Bteam = 0 #b팀 능력치
    for j in range(N//2):
        player = team[-i-1][j]
        for k in team[-i-1]:
            Bteam += S[player][k]

    mingap = min(mingap, abs(Ateam-Bteam))

print(mingap)

'''
N명의 사람 중 N/2 를 뽑고 모두 능력치 계산해서 제일 작은거 찾아보면 됨
nC(n/2)
1,2 뽑나 2,1 뽑나 같은 팀이기 때문에 C(조합) 사용
'''