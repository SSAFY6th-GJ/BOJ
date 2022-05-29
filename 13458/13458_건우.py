N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in A:
  if B >= i:
    answer += 1
  else:
    answer += 1
    i -= B
    if i % C > 0:
      answer += (i //C) + 1
    else:
      answer += i // C
print(answer)

