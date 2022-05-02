N = int(input())
K = int(input())
lst = list(map(int, input().split()))
lst.sort()
# 1 3 6 6 7 9   # 차이가 2 3 0 1 2   -> 0 1 2 2 3
# 3 6 7 8 10 12 14 15 18 20   # 차이가 3 1 1 2 2 2 1 3 2   -> 1 1 1 2 2 2 2 3 3