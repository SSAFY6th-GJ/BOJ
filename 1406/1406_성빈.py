import sys
input = sys.stdin.readline

first = list(input().strip())
result = []
# print(first)
m = int(input())
now = len(first)
for i in range(m):
    command = input().strip()
    # print(command[2])
    if command[0] == 'L' and len(first) != 0:
        # now -= 1
        result.append(first.pop())
    elif command[0] == 'D' and len(result) != 0:
        # now += 1
        first.append(result.pop())
    elif command[0] == 'B' and len(first) != 0:
        # del first[now-1]
        # now -= 1
        first.pop()
    elif command[0] == 'P':
        # print(command[2])
        # first.insert(now, command[2])
        # now += 1
        first.append(command[2])

first.extend(result[::-1])

print(''.join(first))

'''
insert, del 보다 append, pop이 시간이 덜 걸린다.
'''