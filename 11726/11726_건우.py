n = int(input())

box = [0] * 1001
box[1] = 1
box[2] = 2
for i in range(3,1001):
  box[i] = box[i-1] + box[i-2]
print(box[n])