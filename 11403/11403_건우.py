N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * N for _ in range(N)]
def dfs(x):    # dfs로 탐색해 나가며 경로를 다찾아서 answer 값을 바꿔준다.
  st = []
  for j in range(N):
    if arr[x][j] == 1:
      st.append(j)
      answer[x][j] = 1
  while st:
    i = st.pop()
    for j in range(N):
      if arr[i][j] == 1 and answer[x][j] == 0:
        st.append(j)
        answer[x][j] = 1

for column in range(N):
  dfs(column)
for k in answer:
  print(*k)
