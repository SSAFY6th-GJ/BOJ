N = int(input())
wine = [0] * 10001
for i in range(N):
    wine[i] = int(input())

d = [0] * 10001
d[0] = wine[0]
d[1] = wine[0] + wine[1]
d[2] = max(d[1], wine[1]+wine[2], wine[0]+wine[2])
for i in range(3, N):
    # wine에서 안겹치게 그리고 연속된 3개가 선택이 안나오도록 조심(2개 차이나게 설정)
    d[i] = max(wine[i]+d[i-2],  wine[i]+wine[i-1]+d[i-3], d[i-1])
print(d[N-1])