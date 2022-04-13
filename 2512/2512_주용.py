
# 이분탐색
N = int(input())                # 지방의 수
budget = list(map(int, input().split()))    # 요청한 예산들
M = int(input())                # 예산
start, end = 0, max(budget)
while start <= end:
    money = 0
    mid = (start + end) // 2    # 중간 지점 잡고
    for i in budget:            # 예산 요청한거 반복문 돌면서
        if mid < i:             # 중간보다 큰게 나오면
            money += mid        # 결과값에 중간값 더하기
        else:                   # 중간보다 작은게 나오면
            money += i          # 결과값에 중간값보다 작은 i 더하기
    if money <= M:              # 상한금액보다 결과값이 작으면
        start = mid + 1         # 시작금액을 1 늘려준다
    else:                       # 상함금액보다 결과값이 크면
        end = mid -1            # 마지막금액을 1 낮춘다
print(end)