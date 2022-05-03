N = int(input())

# 2*1 -> 1
# 2*2 -> 2
# 2*3 -> 3
# 2*4 -> 5
# 2*5 -> 8
paint = [0, 1, 2, 3]
for x in range(3, 1000):
    paint.append(paint[x-1]+paint[x])
print(paint[N] % 10007)