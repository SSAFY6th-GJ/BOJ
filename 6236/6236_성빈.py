import sys
input = sys.stdin.readline

N, M = map(int, input().split())
account = []
for _ in range(N):
    account.append(int(input()))

start, end = max(account), sum(account)
k = end
while start <= end:
    mid = (start+end)//2 # 인출할 돈
    now = mid # 현재 가지고 있는 돈
    draw = 1 # 인출 횟수
    for i in account: # N일 동안 쓸 돈 반복문
        if now < i: # 현재 가지고 있는 돈보다 하루 쓸 돈이 부족하면 돈을 뽑아야함
            now = mid
            draw += 1 # 인출횟수 +1
        now -= i # 현재 가지고 있는 돈으로 그날 쓸 돈 씀

    if draw > M or mid < max(account): # M번보다 돈을 더 많이 인출하거나 뽑은 돈이 부족할 경우
        start = mid+1
    else: # 인출횟수가 M번 보다 적거나 같음 / 인출 금액이 많음
        end = mid-1
        k = mid

print(k)

'''
인출하는 돈이 하루 쓸 돈보다 작으면 안된다.
N개의 수가 주어지고 이를 합이 K이하인 M개의 그룹으로 묶는다.
M은 고정된 상수이며, K의 최솟값을 찾아라.
이분탐색을 돌려서 K 값을 기준으로 몇개의 그룹으로 나누어지는지 찾는다.
나누어진 그룹의 수가 M보다 크면 정답이 아님. M보다 작거나 같아야함
'''