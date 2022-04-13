N = int(input())
stairs = [0]*301
for i in range(N):
  stairs[i] = int(input())

score = [0] * 301
score [0] = stairs[0]
score [1] = stairs[0] + stairs[1]
score [2] = max(stairs[0]+ stairs[2], stairs[1]+stairs[2])
for j in range(3, N):
  score[j] = max(score[j-2]+ stairs[j], score[j-3]+stairs[j-1]+stairs[j])

print(score[N-1])