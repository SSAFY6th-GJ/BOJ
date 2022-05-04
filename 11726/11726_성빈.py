import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def answer(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return answer(num-1) + answer(num-2)

n = int(input())
print(answer(n)%10007)

'''
2x1 ㅁ : l  -> 1개

2x2 ㅁ : ll, = -> 2개 

2x3 ㅁ : lll, =l, l= -> 3개 

2x4 ㅁ : llll, =ll, l=l, ll=, == -> 5개 

9095번 문제랑 완전 똑같다.
런타임에러가 나서 3번줄 코드를 추가하여 재귀 깊이를 늘려줬는데
시간초과 뜸 ;
'''