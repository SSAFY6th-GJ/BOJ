from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():
  que = deque(virus)
  count = 0
  while que:
    if count == S:
      break
    for _ in range(len(que)):
      cur_i, cur_j = que.popleft()
      for d in range(4):
        new_i = cur_i + di[d]
        new_j = cur_j + dj[d]
        if 0<= new_i < N and 0 <= new_j < N and arr[new_i][new_j] == 0:
          arr[new_i][new_j] = arr[cur_i][cur_j]
          que.append((new_i,new_j))
    count+= 1
  return arr[X-1][Y-1]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
temp_virus = []
for i in range(N):
  for j in range(N):
    if arr[i][j] != 0:
      temp_virus.append((arr[i][j],i,j))
temp_virus.sort()     #temp _virus 추가된 데이터는 바이러스의 번호 순서대로 들어온 것이 아니기 때문에 sort로  정렬해준다.
# print(temp_virus)
virus = []
for n in range(len(temp_virus)):
  virus.append(temp_virus[n][1:])   # 정렬된 temp_virus에서 좌표값만 저장해준다.
print(bfs())