import sys
input = sys.stdin.readline

n = int(input())
money = list(map(int, input().split()))
m = int(input()) # 예산
# print(money)
# left = min(money)
left = 0
right = max(money)

if sum(money) <= m:
    print(max(money))
else:
    while(left <= right):
        mid = (left+right)//2
        res = 0 # 총 지출
        for i in money:
            if (i<=mid):
                res += i
            else:
                res += mid
        if (res>m): # 지출 양이 예산보다 크ㄷ면
            right = mid-1
        elif (res<=m): # 지출 양이 예산보다 적으면
            left = mid+1
    print(right)