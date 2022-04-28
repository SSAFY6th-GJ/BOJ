import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

e, f = 0, 0

f = b*d
a = a*d
b = b*c
e = a+b

# 최대공약수
gcd = math.gcd(e, f) # math.gcd(숫자1, 숫자2) = 숫자1이랑 숫자2의 최대공약수를 반환해줌
e //= gcd
f //= gcd
print(e, f)

# if e > 1:
#     for i in range(e, 0, -1):
#         if f % i == 0 and e % i == 0:
#             print(e//i, f//i)
#             break
# else:
#     print(e, f)


