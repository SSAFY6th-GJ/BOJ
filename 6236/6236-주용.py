import sys
sys.stdin = open('용돈관리.txt')
# N일 동안 M번만 통장에서 돈을 빼서 쓰기
# 통장에서 K원 인출
N, M = map(int, input().split())
money = list(int(input()) for _ in range(N))
min_money = min(money)
sum_money = sum(money)      # max로 했었는데 max로 하면 틀린 이유는 min~max 사이에서 움직이니까
                            # max보다 작게되면 max때 못쓴다
K = 0
while min_money <= sum_money:
    mid_money = (min_money + sum_money) // 2
    mid = mid_money             # 중간값
    cnt = 1                     # cnt가 1인 이유는 일단 이전꺼 회수 후 K만큼 다시 받아서 쓰니까 1부터 시작
    for x in range(len(money)):
        if money[x] > mid:      # 써야할 돈보다 남은 돈이 더 적으면
            mid = mid_money     # 남은 돈을 통장에 넣고 중간값으로 할당
            cnt += 1            # 횟수 추가
        mid -= money[x]         # 그날 쓰는 돈 빼기
    if cnt > M or mid_money < max(money):# cnt가 M보다 더 많다는 건 중간값 금액을 더 높여야 한다.
                    # 그리고 중간값보다 최댓값이 높으면 안된다.(모자라면 반납하고 쓰는거니까 똑같이 부족한 상태)
        min_money = mid_money + 1
    else:
        sum_money = mid_money - 1
        K = mid_money   # 들여쓰기하면 시간초과 ..왜나지?
print(K)