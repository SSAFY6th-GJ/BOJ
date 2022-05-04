# 원으로 생각해보자
N = int(input())
for _ in range(N):
    answer = 0
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2)
    if distance == 0: # 같은 위치
        if r1 == r2:  # 거리가 같으면 어디든 갈 수 있다(무한대)
            answer = -1
        else:         # r1과 r2가 다르면 경우의 수가 없다
            answer = 0
    else:    # 다른 위치
        if abs(r2-r1) < distance < r2+r1:     # 두번 겹친다
            answer = 2
        elif abs(r2-r1) == distance or r2+r1 == distance: # 접할때
            answer = 1
        else:                   # 아예 겹치는 곳이 없다
            answer = 0
    print(answer)