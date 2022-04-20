import sys
input = sys.stdin.readline

N = input().rstrip() # 이동하려고 하는 채널
# print(len(N))
M = int(input()) # 고장난 버튼의 개수
lst = []
if M != 0:
    lst = list(map(int, input().split()))

if N == '100':
    print(0)
else:
    bnt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if len(lst) != 0:
        for i in lst:
            if i in bnt:
                bnt.remove(i)
    # print(bnt)
    cnt = 0
    num = ''
    for i in N:
        # print(i)
        if int(i) in bnt:
            cnt += 1
            num += i
        else:
            for j in range(1,10):
                if abs(int(i)-j) in bnt:
                    cnt += 1
                    num += str(abs(int(i)-j))
                    break
                elif (int(i)+j) in bnt:
                    cnt += 1
                    num += str(int(i)+j)
                    break
    cnt += abs(int(num)-int(N))
    print(num)
    print(cnt)

'''
1. 고장난 버튼이 없을때랑 있을때
2. 이동하려는 채널이 100일때는 움직일 필요가 없음

고장난버튼이 있을때
0~9에서 고장난버튼을 지워준다.
누를 수 있는 버튼 리스트에서 이동하려는 채널의 버튼을 누를 수 있으면 +1
없으면 차이가 가장 작은 거부터 찾아서 +1 (그 버튼 누르는 횟수 1번)
마지막에 최종적으로 이동 가능한 채널번호를 구해서
그 채널 번호와 이동하려는 번호의 차를 구해서 cnt에 더해준다.

예제 7번만 틀림
'''