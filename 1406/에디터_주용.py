import sys

start = list(sys.stdin.readline().rstrip())
# 문제 유형에 stack 있어서 stack 활용해봤다
stack1 = []
res = ''
N = int(sys.stdin.readline())
order = [sys.stdin.readline().rstrip() for _ in range(N)]
# 커서를 왼쪽으로 움직인다? 그러면 커서 왼쪽으로 움직이고 커서기준 오른쪽 글자는 stack1으로 보낸다.
for x in order:
    if x[0] == 'P':
        start.append(x[2])
    elif x == 'L':
        if start:
            stack1.append(start.pop())
    elif x == 'D':
        if stack1:
            start.append(stack1.pop())
    elif x == 'B':
        if start:
            start.pop()

for x in start:
    res += x
for y in range(len(stack1)-1, -1, -1):
    res += stack1[y]
# start.extend(reversed(stack1))
# print(''.join(start))
print(res)