import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    count = 0

    arr = []

    for i in range(1, 4):
        while n != 0:
            n -= i
            arr.append(i)
