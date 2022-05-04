import sys
input = sys.stdin.readline

def answer(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return answer(num-1) + answer(num-2) + answer(num-3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(answer(n))

'''
정수 1 -> 1 -> 1개
정수 2 -> (1+1), 2 -> 2개
정수 3 -> (1+1+1), (1+2), (2+1), 3 -> 4개
정수 4 -> (1+1+1+1), (1+1+2), (1+2+1), (1+3), (2+1+1), (2+2), (3+1) -> 7개
정수 5 -> 정수 2 + 정수 3 + 정수 4 -> 13개
...
'''