gears = [list(map(int, input())) for _ in range(4)]
k = int(input())
for _ in range(k):
  pos, direct = map(int,input().split())
  pos = pos - 1
  rotating_direct = [0, 0, 0, 0]
  # 왼쪽에 있는 애들 체크
  rotating_direct[pos] = direct
  for i in range(pos-1,-1,-1):
    if gears[i][2] != gears[i+1][6]:
      rotating_direct[i] = rotating_direct[i+1] * -1
    else:
      break
  #오른쪽에 있는애들 체크
  for j in range(pos+1,4):
    if gears[j][6] != gears[j-1][2]:
      rotating_direct[j] = rotating_direct[j-1] * -1
    else:
      break
  for k in range(4):
    if rotating_direct[k] == 1:  #시계방향으로 회전
      gears[k] = [gears[k][7]] + gears[k][0:7]
    elif rotating_direct[k] == -1: # 반시계방향으로 회전
      gears[k] = gears[k][1:8] +[gears[k][0]] 

answer = 0
if gears[0][0] == 1:
  answer += 1
if gears[1][0] == 1:
  answer += 2
if gears[2][0] == 1:
  answer += 4
if gears[3][0] == 1:
  answer += 8
print(answer)
