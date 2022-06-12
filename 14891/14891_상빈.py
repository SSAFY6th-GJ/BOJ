def rolling_gear(n, d):
    if d == 1:
        gear[n] = [gear[n][-1]] + gear[n][:-1]
    elif d == -1:
        gear[n] = gear[n][1:] + [gear[n][0]]


def prepare(n, d):

    roll_soon = [0, 0, 0, 0]                            # 톱니바퀴들이 어느방향으로 돌아갈지 저장하는 배열

    roll_soon[n] = d

    for i in range(n, 3, 1):                            # 오른쪽 톱니바퀴 확인
        if gear[i][2] != gear[i+1][6]:
            roll_soon[i+1] = roll_soon[i] * (-1)

    for i in range(n, 0, -1):                           # 왼쪽 톱니바퀴 확인
        if gear[i][6] != gear[i-1][2]:
            roll_soon[i-1] = roll_soon[i] * (-1)

    for i in range(4):                                  # 배열에 저장한대로 돌려주기
        if roll_soon[i] != 0:
            rolling_gear(i, roll_soon[i])


gear = [list(input()) for _ in range(4)]

K = int(input())
for _ in range(K):
    gear_no, direction = map(int, input().split())
    prepare(gear_no-1, direction)

ans = 0
for i in range(4):
    if gear[i][0] == '1':
        ans += 2**i

print(ans)