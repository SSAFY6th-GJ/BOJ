# 왜 답이 안나오지

N = int(input())
M = int(input())
if M > 0:
    buttons = list(input().split())
    print(buttons)
else:
    buttons = []
simple = abs(100 - N)  # 100에서 방향으로 단순 번호 이동
for x in range(1000001): # 1000001 인 이유는 4, 5가 고장이 났을때 500000번을 누르려면 600000이 제일 가까운 번호이니까
    for y in str(x):
        if y in buttons:
            break
    simple = min(simple, len(str(x))+ abs(N-x)) # 근처 번호로 이동해서 방향이동
print(simple)