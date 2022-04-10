import sys
input = sys.stdin.readline

n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))



'''
포도주 3잔을 연속으로 마실 수 없다.
ㅁ + X + ㅇ + ㅇ
     ㅁ + X + ㅇ
         ㅁ + X
'''