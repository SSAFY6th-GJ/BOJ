# 0번 인덱스에 위치한 것은 무조건 더해줘야한다. why? 처음에는 숫자로 시작하니까 음수가 나올 수 없음
# 55-50+40
math_expression = input().split('-')    # ['55', '50+40']
res = 0
for x in math_expression[0].split('+'): # 0번 인덱스니까 더해주기.
    res += int(x)
for x in math_expression[1:]:   # 그 이후에 나오는거는 모두 - (         )   -괄호 안에 있다고 생각해야 최소 숫자가 나온다
    for y in x.split('+'):
        res -= int(y)
print(res)