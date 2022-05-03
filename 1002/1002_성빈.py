import sys
input = sys.stdin.readline
import math

T = int(input())
for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())

    distance = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2) # 두 점 사이 거리

    if distance == 0: # 두 점이 같을 때
        if r_1 == r_2: # 두 원이 아예 똑같을 때
            print(-1)
        else: # 한 원이 다른 원 안에 들어가 있는 경우
            print(0)
    else: # 두 점이 다를 때
        if r_1+r_2 == distance or abs(r_2-r_1) == distance:
            print(1)
        elif ((abs(r_1-r_2) < distance) and (distance < r_1+r_2)):
            print(2)
        else:
            print(0)