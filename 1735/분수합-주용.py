A, B = map(int, input().split())    # 분자 분모
C, D = map(int, input().split())

# 유클리드호제법
# 각 분모의 최대공약수 구하기
def choiso(a, b):
    while a % b != 0:
        x = a % b
        a = b
        b = x
    return b
tmp = choiso(B, D)  # 최대공약수
x, y = C*(B // tmp) , ( tmp * (B // tmp) * (D // tmp) )
z, i = A*(D // tmp), ( tmp * (B // tmp) * (D // tmp) )
t = choiso(x+z, y)
print( (x+z) // t, y // t)