di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i, j, num):
  

  cur_i, cur_j = i, j
  num += str(arr[cur_i][cur_j])
  if len(num) == 6:
    if num not in res:
      res.append(num)
    return
  for d in range(4):
    new_i = cur_i + di[d]
    new_j = cur_j + dj[d]
    if 0 <= new_i < 5 and 0 <= new_j < 5:
      bfs(new_i, new_j, num)



arr = [list(map(int, input().split())) for _ in range(5)]
res=[]
for row in range(5):
  for col in range(5):
    bfs(row,col,'')
print(len(res))