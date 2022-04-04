import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    # print(lst)

    maxv = 0
    for i in range(n-2):
        maxv = max(maxv, abs(lst[i]-lst[i+2]))
    last = abs(lst[-1]-lst[-2])
    maxv = max(maxv, last)

    print(maxv)

'''
가장 큰 통나무를 가운데를 기준으로 넣고
그 다음 크기 순대로 양 옆을 채워나가면 된다.
처음에는 직접 위의 순서대로 리스트를 채우려 했는데 너무 어려워서
오름차순으로 정렬한 후 2 인덱스 차이 씩 빼주었다.
'''
'''
[0,2,4,3,1]
'''
